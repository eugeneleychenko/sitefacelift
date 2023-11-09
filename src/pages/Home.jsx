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

function Home() {
  return (
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
      <section className="container">
        <BlogPosts />
      </section>
      <section>
        <Members />
      </section>
      <section className="container">
        <Experience />
      </section>
      <hr />
      <section className="container">
        <Appointment />
      </section>
      <section>
        <Footer />
      </section>
    </div>
  );
}

export default Home;
