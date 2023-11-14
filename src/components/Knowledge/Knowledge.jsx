import React, {useContext} from "react";
import styles from "./Knowledge.module.css";
import { AppContext } from '../../context/AppContext';



function Knowledge() {
  const {valueProp, CTA } = useContext(AppContext);
  
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
