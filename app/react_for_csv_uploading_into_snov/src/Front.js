import React, { useState, useEffect } from "react";
import {
  TextField,
  Button,
  Badge,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Box,
  Grid,
  Divider,
  Typography,
  Accordion,
  Tooltip,
  AccordionSummary,
  AccordionDetails,
} from "@mui/material";

import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

const Front = () => {
  const [userLists, setUserLists] = useState([]);
  const [selectedList, setSelectedList] = useState("");
  const [domain, setDomain] = useState("");
  const [emails, setEmails] = useState([]);
  const [names, setNames] = useState({});
  const [disabledEmails, setDisabledEmails] = useState({}); // New state to track disabled emails
  const [attorneyNames, setAttorneyNames] = useState(); // New state to store attorney names as a string
  const [navLinks, setNavLinks] = useState([]);
  const [tempNavLinks, setTempNavLinks] = useState("");

  const endPoint = "http://127.0.0.1:5000/";

  useEffect(() => {
    // Fetch user lists on component mount
    fetch(`${endPoint}user_lists`)
      .then((response) => response.json())
      .then((data) => {
        // Transform the data to a format suitable for the dropdown
        const transformedData = data.map(({ id, name }) => ({
          value: id,
          label: name,
        }));
        setUserLists(transformedData);
        // console.log(transformedData); // Log to see if data is correctly transformed
      })
      .catch((error) => console.error("Error fetching user lists:", error));
  }, []);

  useEffect(() => {
    console.log("emails", emails);
  }, [emails]);

  useEffect(() => {
    console.log("Names of attorneys:", attorneyNames);
  }, [attorneyNames]);

  useEffect(() => {
    // Whenever navLinks changes, update tempNavLinks to reflect the current state
    setTempNavLinks(navLinks.join("\n"));
    console.log(navLinks);
  }, [navLinks]);

  const handleNavLinksChange = (event) => {
    setTempNavLinks(event.target.value);
  };

  const updateNavLinks = () => {
    // Split the tempNavLinks by newline to convert back to array and update navLinks state
    setNavLinks(tempNavLinks.split("\n"));
  };

  const handleDomainSearch = () => {
    fetch(`${endPoint}ping_snov/${domain}`)
      .then((response) => response.json())
      .then((data) => {
        setEmails(data);
        console.log(emails);
      })
      .catch((error) => console.error("Error searching domain:", error));
  };

  const handleAddProspect = async (email) => {
    const name = names[email];
    try {
      const tokenResponse = await fetch(`${endPoint}get_snov_token`);
      const tokenData = await tokenResponse.json();
      const accessToken = tokenData.access_token;

      const response = await fetch(
        "https://api.snov.io/v1/add-prospect-to-list",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            access_token: accessToken,
            email: email,
            firstName: name,
            listId: selectedList,
          }),
        }
      );
      const data = await response.json();
      console.log(data);

      // Check if the prospect was added successfully and update the disabledEmails state
      if (data.added) {
        setDisabledEmails((prevState) => ({ ...prevState, [email]: true }));
      }
    } catch (error) {
      console.error("Error adding prospect:", error);
    }
  };

  const handleNameChange = (email, name) => {
    setNames({ ...names, [email]: name });
  };

  const extractAttorneysFromDomain = () => {
    fetch(`${endPoint}extract_attorneys_from_domain/${domain}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log("Received data:", data); // Added for more detailed logging
        if (data.attorneys === undefined || data.navLinks === undefined) {
          console.error("Undefined attorneys or navLinks in response:", data);
        } else {
          console.log("Attorneys extracted:", data.attorney_names);
          console.log("Navigation links:", data.all_nav_links);
        }

        setAttorneyNames(data.attorney_names || []); // Fallback to empty array if undefined
        setNavLinks(data.all_nav_links || []); // Fallback to empty array if undefined
      })
      .catch((error) => {
        console.error("Error fetching attorney names:", error);
        console.error("Additional error details:", error.message);
        setAttorneyNames([]); // Reset to empty array or handle as needed
        setNavLinks([]);
      });
  };

  const matchEmailstoNames = async () => {
    try {
      const response = await fetch(`${endPoint}match_emails_with_names`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          emails: emails,
          attorneyNames: attorneyNames,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Success:", data);
      const updatedNames = data.matches.reduce((acc, { email, name }) => {
        acc[email] = name;
        return acc;
      }, {});

      // Set the updated names in the state
      setNames(updatedNames);
    } catch (error) {
      console.error("Error sending data to backend:", error);
    }
  };

  const buildTheSite = () => {
    console.log("Placeholder function for building the site.");
    // Placeholder implementation
    // This function is intended to build or reconstruct the site based on certain criteria.
    // The actual implementation will depend on the specific requirements and setup.
  };

  return (
    <Grid container spacing={2}>
      <Grid item xs={4} sx={{ height: "100vh", overflow: "hidden" }}>
        {" "}
        {/* Sidebar takes up 33% (4/12) of the width */}
        <Box sx={{ p: 6, backgroundColor: "#d3d3d31f", height: "100vh" }}>
          <FormControl fullWidth>
            <InputLabel id="list-select-label">Select a List</InputLabel>
            <Select
              labelId="list-select-label"
              value={selectedList}
              label="Select a List"
              onChange={(e) => setSelectedList(e.target.value)}
            >
              {userLists.map((list) => (
                <MenuItem key={list.value} value={list.value}>
                  {list.label}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          <Tooltip
            placement="left"
            title="Searches Snov for emails matching the domain"
          >
            <Badge badgeContent={emails.length} color="secondary">
              <Button
                variant="contained"
                onClick={handleDomainSearch}
                sx={{ alignSelf: "flex-start", mt: "10px" }}
              >
                Domain Search and Return Emails
              </Button>
            </Badge>
          </Tooltip>
          <Tooltip
            placement="left"
            title="Scrapes site and returns names of Attorneys"
          >
            <Badge
              badgeContent={attorneyNames ? attorneyNames.split(",").length : 0}
              color="secondary"
            >
              <Button
                variant="contained"
                onClick={extractAttorneysFromDomain}
                sx={{ alignSelf: "flex-end", mt: "10px" }}
              >
                Find Names of Attorneys
              </Button>
            </Badge>
          </Tooltip>
          <Badge
            badgeContent={navLinks ? navLinks.length : 0}
            color="secondary"
          >
            <Button
              disabled
              variant="contained"
              sx={{ alignSelf: "flex-end", m: "10px" }}
            >
              Find Nav Links
            </Button>
          </Badge>
          <Tooltip
            placement="left"
            title="In this app, matches emails to first names"
          >
            <Button
              variant="contained"
              onClick={matchEmailstoNames}
              sx={{ alignSelf: "flex-end", mt: "10px" }}
            >
              Match Emails to Names
            </Button>
          </Tooltip>

          <Button
            variant="contained"
            onClick={buildTheSite}
            sx={{ alignSelf: "flex-end", m: "10px" }}
          >
            Build The Site
          </Button>
        </Box>
      </Grid>
      <Grid item xs={8} sx={{ height: "100vh", overflowY: "auto" }}>
        {" "}
        {/* Scrollable right section */}{" "}
        {/* Main content takes up the remaining 67% */}
        <Box
          sx={{
            p: 2,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Box
            sx={{
              width: "100%",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              mb: 2,
            }}
          >
            <Box
              sx={{
                width: "100%",
                display: "flex",
                flexDirection: "row", // Change this to row to align items horizontally
                alignItems: "center",
                mb: 2,
              }}
            ></Box>
            <TextField
              fullWidth
              label="Domain"
              value={domain}
              onChange={(e) => setDomain(e.target.value)}
              placeholder="sptaxlaw.com"
              margin="normal"
              sx={{ mr: 2 }} // Add right margin to separate the TextField and Button
              onKeyPress={(e) => {
                if (e.key === "Enter") {
                  handleDomainSearch();
                }
              }}
            />
          </Box>

          <Accordion sx={{ width: "100%", borderRadius: "10px" }}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography
                variant="h6"
                component="div"
                sx={{ fontWeight: "bold" }}
              >
                Email List
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              {emails.map((email, index) => (
                <Box
                  key={index}
                  sx={{
                    width: "100%",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    mb: 2,
                  }}
                >
                  <Typography sx={{ mr: 2, flexShrink: 0 }}>{email}</Typography>
                  <TextField
                    label="Name"
                    sx={{ flexGrow: 1, mr: 2 }}
                    value={names[email] || ""}
                    onChange={(e) => handleNameChange(email, e.target.value)}
                    margin="normal"
                  />
                  <Button
                    variant="contained"
                    onClick={() => handleAddProspect(email)}
                  >
                    Add to List
                  </Button>
                </Box>
              ))}
            </AccordionDetails>
          </Accordion>
          <Typography
            variant="h6"
            component="div"
            sx={{ fontWeight: "bold", mt: "20px" }}
          >
            Nav Links
          </Typography>
          <TextField
            fullWidth
            label="Navigation Links"
            multiline
            rows={4}
            value={tempNavLinks}
            onChange={handleNavLinksChange}
            variant="outlined"
            margin="normal"
          />
          <Button
            variant="contained"
            onClick={updateNavLinks}
            sx={{ alignSelf: "flex-end", m: "10px" }}
          >
            Update
          </Button>
        </Box>
      </Grid>
    </Grid>
  );
};

export default Front;
