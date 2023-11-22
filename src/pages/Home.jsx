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
import { AppContext } from '../context/AppContext';

function Home({ match }) {
  const [data, setData] = useState(null);
  const { domain } = useParams();

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

  if (!data) {
    return null;
  }
  


//Appointment.jsx
const paragraph = data.paragraph;
//Details.jsx
const detailsDataString = "[" + data.detailsData + "]";

// Parse the string into an array of objects
  const detailsData = JSON.parse(detailsDataString);

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
const CTA = data.CTA;
console.log("members", data.members)

const cleanedMemberData = data.members === 'N/A' ? 'N/A' : data.members.replace(/```json\n|\n```/g, '');

const members = cleanedMemberData === 'N/A' ? 'N/A' : JSON.parse(cleanedMemberData);
console.log("members cleaned", members)
//Nav.jsx
const openHours = data.openHours;
const cleanedTestimonalData = data.testimonalData ? data.testimonalData.replace(/```json\n|\n```/g, '') : null;

// Parse the cleaned string into an array of objects if it's not null
const testimonalData = cleanedTestimonalData ? JSON.parse(cleanedTestimonalData) : null;
// const testimonalData = data.testimonalData;
//Lists.js 
// const topics = JSON.parse(data.topics);
const topics = data.topics;

  return (
    <AppContext.Provider value={{ paragraph, detailsData, address, phoneNumber, email, linkNames, companyName, subHeading, valueProp, CTA, topics, members, openHours, testimonalData }}>
      <div>
        <section>
          <HeroSection />
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
  );
}

export default Home;