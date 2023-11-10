import React from "react";
import styles from "./Lists.module.css";
import { Link } from "react-router-dom";

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

function Lists() {
  return (
    <div className={styles.lists}>
      {topics.slice(4).map((topic, index) => (
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
