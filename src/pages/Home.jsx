import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import HeroSection from "../components/HeroSection/HeroSection";
import Knowledge from "../components/Knowledge/Knowledge";
import Topics from "../components/Topics/Topics";
import Lists from "../components/Lists/Lists";
import ParallaxImg from "../components/ParallaxImg/ParallaxImg";
import Details from "../components/Details/Details";
import Testimonial from "../components/Testimonial/Testimonial";
import BlogPosts from "../components/BlogPosts/BlogPosts";
import Members from "../components/Members/Members";
import Experience from "../components/Experience/Experience";
import Appointment from "../components/Appointment/Appointment";
import Footer from "../components/Footer/Footer";
import { AppContext } from "../context/AppContext";
import CTABar from "../components/CTABar/CTABar";

function Home({ match }) {
  const [data, setData] = useState(null);
  const { domain } = useParams();
  const [showCTABar, setShowCTABar] = useState(true);
  const [lastScrollY, setLastScrollY] = useState(0);
  const barHeight = "40";

  useEffect(() => {
    const fetchData = async () => {
      try {
        // const domain = match.params.domain;
        const dataModule = await import(`../data/${domain}/data.json`);
        setData(dataModule.default);
        // console.log(dataModule)
      } catch (err) {
        console.error(err);
      }
    };
    fetchData();
  }, [domain]);

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;
      if (currentScrollY < lastScrollY) {
        setShowCTABar(true);
      } else if (currentScrollY > lastScrollY) {
        setShowCTABar(false);
      }
      setLastScrollY(currentScrollY);
    };

    window.addEventListener("scroll", handleScroll, { passive: true });

    return () => window.removeEventListener("scroll", handleScroll);
  }, [lastScrollY]);

  if (!data) {
    return null;
  }

  //Appointment.jsx
  const paragraph = data.paragraph;
  //Details.jsx
  const detailsDataString = "[" + data.detailsData + "]";

  // Parse the string into an array of objects
  let detailsData;
  try {
    detailsData = JSON.parse(detailsDataString);
  } catch (error) {
    console.error("Parsing error in detailsData", error);
    detailsData = []; // or set a default value
  }

  //Footer.js
  const address = data.address;
  const phoneNumber = data.phoneNumber;
  const email = data.email;

  //Header.js
  const linkNames = data.linkNames;
  // const linkNames = JSON.parse(data.linkNames);

  //HeroSection.jsx
  const companyName = data.companyName;
  const subHeading = data.subHeading;

  //Knowledge.jsx
  const valueProp = data.valueProp;
  const CTA = data.CTA ? data.CTA.toUpperCase() : "";
  console.log("members", data.members);

  let members;
  if (typeof data.members === "string") {
    const cleanedMemberData = data.members.replace(/```json\n|\n```/g, "");
    try {
      members = JSON.parse(cleanedMemberData);
    } catch (error) {
      console.error("Parsing error in members", error);
      members = []; // or set a default value
    }
  } else {
    members = data.members || []; // Use the value if it's not a string, or default to an empty array
  }
  console.log("members cleaned", members);
  //Nav.jsx
  const openHours = data.openHours;
  const cleanedTestimonalData = data.testimonalData
    ? data.testimonalData.replace(/```json\n|\n```/g, "")
    : null;

  // Parse the cleaned string into an array of objects if it's not null
  let testimonalData;
  try {
    testimonalData = cleanedTestimonalData
      ? JSON.parse(cleanedTestimonalData)
      : null;
  } catch (error) {
    console.error("Parsing error in testimonalData", error);
    testimonalData = []; // or set a default value
  }
  // const testimonalData = data.testimonalData;
  //Lists.js
  // const topics = JSON.parse(data.topics);
  const topics = data.topics;

  return (
    <>
      <AppContext.Provider
        value={{
          paragraph,
          detailsData,
          address,
          phoneNumber,
          email,
          linkNames,
          companyName,
          subHeading,
          valueProp,
          CTA,
          topics,
          members,
          openHours,
          testimonalData,
        }}
      >
        {/* <div style={{ paddingTop: barHeight }}> */}
        <div>
          <section>
            <CTABar
              ctaText={
                <span>
                  Love the site?{" "}
                  <a
                    href="https://buy.stripe.com/7sI047bvq7lL6n6eV1"
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ color: "white", textDecoration: "underline" }}
                  >
                    Buy it here
                  </a>
                </span>
              }
              show={showCTABar}
              barHeight={`${barHeight}px`}
            />
          </section>
          <section>
            <HeroSection barHeight={barHeight} />
          </section>
          <section className="container">
            <Knowledge />
          </section>
          <section>
            <Topics />
          </section>
          <hr />
          <section className="container">
            <Lists />
          </section>
          <section>
            <ParallaxImg />
          </section>
          <section>
            <Details />
          </section>
          <section>
            <Testimonial />
          </section>
          <section>
            <Members />
          </section>
          <hr />
          <section className="container">
            <Appointment />
          </section>
          <section>
            <Footer />
          </section>
        </div>
      </AppContext.Provider>
      {/* </div> */}
    </>
  );
}

export default Home;
