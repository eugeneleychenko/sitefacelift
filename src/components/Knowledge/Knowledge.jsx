import React from "react";
import styles from "./Knowledge.module.css";

const valueProp = `Giordano Law Offices Personal Injury & Employment Lawyers is an award winning Harlem-based New York City law firm specializing in Personal Injury, Civil Rights, and Employment Litigation. Giordano Law continues to win awards like Super Lawyers year after year because of our experience and high-level of care for our clients. Over decades, our top rated firm has recovered millions of dollars for clients. For injury and some employment cases, you will not have to pay a fee unless we are successful and get a recovery for you. \nCall or text us today, we will never charge you for an initial consultation. With Us, It’s Personal.`
const CTA = "BOOK YOUR FREE CONSULTATION NOW   "

function Knowledge() {
  
  
  return (
    <div className={styles.knowledge}>
      <div className={styles.knowledgeLeft} data-aos="fade-right">
        <h5>KNOWLEDGE AND EXPERTISE</h5>
        <h1>You've Come To The Right Place</h1>
      </div>
      <div className={styles.knowledgeRight} data-aos="fade-left">
        <p>
         {valueProp}
        </p>
        <button className={`btn ${styles.button}`}>{CTA}</button>
      </div>
    </div>
  );
}

export default Knowledge;
