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
    title: "EXCELLENT TRACK RECORD",
    content:
      "Our award-winning attorneys have recovered over $20 Million dollars for our clients. You won't find tougher advocates.",
  },
  {
    url: "/",
    title: "TRANSPARENT FEES",
    content:
      "Consultations are always free and we take all personal injury cases on a contingency basis, meaning, you will not be charged until we are successful at obtaining a recovery for you.",
  },
  {
    url: "/",
    title: "UNPARALLELED CUSTOMER SERVICE",
    content:
      "You are not just a number at our firm. When you become our clients, you have unparalleled access to our attorneys and we are available 24/7 for you.",
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
