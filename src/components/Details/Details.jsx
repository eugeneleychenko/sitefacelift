import React from "react";
import styles from "./Details.module.css";
import listMarkIcon from "../../assets/check-box-h2.png";
import detailsImg1 from "../../assets/details-1.jpg";
import detailsImg2 from "../../assets/details-2.jpg";
import { Link } from "react-router-dom";

// Define your data object with URL and content
const detailsData = [
  {
    url: "/",
    title: "Company Commercial",
    content:
      "At vero eos et accusamus et justo odio blanditiis similique in culpa.",
  },
  {
    url: "/",
    title: "Intellectual Property",
    content:
      "At vero eos et accusamus et justo odio blanditiis similique in culpa.",
  },
  {
    url: "/",
    title: "Personal Injury",
    content:
      "At vero eos et accusamus et justo odio blanditiis similique in culpa.",
  },
  {
    url: "/",
    title: "Consumer Rights",
    content:
      "At vero eos et accusamus et justo odio blanditiis similique in culpa.",
  },
];

function Details() {
  return (
    <div className={styles.details}>
      <div className={styles.leftDetails}>
        {detailsData.map((item, index) => (
          <div key={index} data-aos="zoom-in">
            <div className={styles.itemTitle}>
              <img src={listMarkIcon} alt="Mark Icon" />
              <h2>{item.title}</h2>
            </div>
            <p>{item.content}</p>
            <Link to={item.url}>VIEW MORE</Link>
          </div>
        ))}
      </div>
      <div className={styles.rightDetails}>
        <img src={detailsImg1} alt="Details 1" data-aos="zoom-out-left"/>
        <img src={detailsImg2} alt="Details 2" data-aos="zoom-out-left"/>
      </div>
    </div>
  );
}

export default Details;
