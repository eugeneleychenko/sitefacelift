import React from "react";
import styles from "./Topics.module.css";

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
  function Topics() {
  return (
    <div className={styles.topics}>
      {topics.slice(0, 4).map((topic, index) => (
        <div key={index} data-aos="fade-right" data-aos-anchor-placement="center-bottom">
          <img
            loading="lazy"
            width="400"
            height="605"
            src={topic.img}
            class="attachment-full size-full"
            alt="a"
            decoding="async"
          />
          <h4>{topic.title}</h4>
        </div>
      ))}
    </div>
  );
}

export default Topics;