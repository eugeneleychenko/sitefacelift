import React from "react";
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






function Home() {
  //Appointment.jsx
  const paragraph = "Call or text (646) 217-0749 to get a free consultation"
  //Details.jsx
  const detailsData = [
    {
      title: "EXCELLENT TRACK RECORD",
      content:
        "Our award-winning attorneys have recovered over $20 Million dollars for our clients. You won't find tougher advocates.",
    },
    {
      title: "TRANSPARENT FEES",
      content:
        "Consultations are always free and we take all personal injury cases on a contingency basis, meaning, you will not be charged until we are successful at obtaining a recovery for you.",
    },
    {
      title: "UNPARALLELED CUSTOMER SERVICE",
      content:
        "You are not just a number at our firm. When you become our clients, you have unparalleled access to our attorneys and we are available 24/7 for you.",
    },
  ];


  return (
    <AppContext.Provider value={{ paragraph, detailsData }}>
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
      {/* <section className="container">
        <BlogPosts />
      </section> */}
      <section>
        <Members />
      </section>
      {/* <section className="container">
        <Experience />
      </section> */}
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
