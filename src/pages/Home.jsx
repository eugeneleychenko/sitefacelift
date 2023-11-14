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
//Footer.js
const address = "226 Malcolm X Blvd, New York, NY 10027"
const phoneNumber = "(646) 217-0749"
const email = "Info@Gio-Law.com"

//Header.js
const linkNames = ["ABOUT", "PRACTICE AREAS", "OUR TEAM", "CASE RESULTS", "TESTIMONIALS","BLOG","CONTACT"
];

//HeroSection.jsx
const companyName = "Giordano Law Offices"
const subHeading = "Personal Injury & Employment Lawyers"

//Knowledge.jsx
const valueProp = `Giordano Law Offices Personal Injury & Employment Lawyers is an award winning Harlem-based New York City law firm specializing in Personal Injury, Civil Rights, and Employment Litigation. Giordano Law continues to win awards like Super Lawyers year after year because of our experience and high-level of care for our clients. Over decades, our top rated firm has recovered millions of dollars for clients. For injury and some employment cases, you will not have to pay a fee unless we are successful and get a recovery for you. \nCall or text us today, we will never charge you for an initial consultation. With Us, It’s Personal.`
const CTA = "BOOK YOUR FREE CONSULTATION NOW   "

//Members.js
const members = [
  {
    name: "Carmen 'Jack' Giordano, Esq.",
    position: "Principal Attorney",
  },
  {
    name: "Stefanie Behler Soriano, Esq.",
    position: "Associate Attorney",
  },
  {
    name: "Brian Robinson, Esq.",
    position: "Of Counsel",
  },
  {
    name: "Toni Marie Angeli, Esq.",
    position: "Of Counsel"
  }
];
//Nav.jsx
const openHours = "Monday to Friday: 10.00 AM – 8.00 PM"

//Testimonial.jsx
const testimonalData = [
  {
    text: `"Carmen was absolutely wonderful to work with. He was truly honest and I never felt taken advantage of. I can't recommend this law office and Carmen enough."`,
    author: "Jaime Oliver",
    location: "New York",
  },
  {
    text: `"Even after the case we still keep in contact for any question that we still might have, for people who do not speak English I recommend him, he makes sure that the person in the case understands everything that happens in their case."`,
    author: "Atriz R",
    location: "Manhattan, New York",
  },
  {
    text: `"When you go to their office you feel like you are home, they treat you like family, with empathy and professionalism; They are simply the best! I totally recommend this law firm. If you need reliable, experienced, and professional representation in your case, this is the right place to come, Giordano Law offices!"`,
    author: "Jesus Antonio M.",
    location: "Bronx, New York",
  },
];
//Lists.js 
const topics = [
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-1.jpg",
      title: "EMPLOYMENT LAW",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-2.jpg",
      title: "PERSONAL INJURY",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-3.jpg",
      title: "GENERAL LITIGATION",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-4.jpg",
      title: "WRONGFUL DEATH",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-5.jpg",
      title: "CIVIL RIGHTS",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-6.jpg",
      title: "DISCRIMINATION",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-7.jpg",
      title: "ENTERTAINMENT",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-8.jpg",
      title: "SEXUAL HARASSMENT",
    },
    {
      img: "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-9.jpg",
      title: "WRONGFUL TERMINATION",
    },
  ];


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
