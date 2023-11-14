import React from "react";
import styles from "./Lists.module.css";
import { Link } from "react-router-dom";

const baseImgUrl = "https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-";

const topics = [
  "EMPLOYMENT LAW",
  "PERSONAL INJURY",
  "GENERAL LITIGATION",
  "WRONGFUL DEATH",
  "CIVIL RIGHTS",
  "DISCRIMINATION",
  "ENTERTAINMENT",
  "SEXUAL HARASSMENT",
  "WRONGFUL TERMINATION",
];

const topicsWithImages = topics.map((title, index) => ({
  img: `${baseImgUrl}${index + 1}.jpg`,
  title,
}));

function Lists() {
  return (
    <div className={styles.lists}>
      {topicsWithImages.slice(4).map((topic, index) => (
        <div key={index}>
          <span>{String(index + 1).padStart(2, '0')}</span>
          <Link>
            <h1>{topic.title.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.substring(1)).join(' ')}</h1>
          </Link>
        </div>
      ))}
    </div>
  );

}

export default Lists;
