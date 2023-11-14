import React, {useContext} from "react";
import styles from "./Topics.module.css";
import { AppContext } from '../../context/AppContext';
  
  function Topics() {

  const {topics } = useContext(AppContext);  
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