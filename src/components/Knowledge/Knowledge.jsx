import React from "react";
import styles from "./Knowledge.module.css";
function Knowledge() {
  return (
    <div className={styles.knowledge}>
      <div className={styles.knowledgeLeft} data-aos="fade-right">
        <h5>KNOWLEDGE AND EXPERTISE</h5>
        <h1>You've Come To The Right Place</h1>
      </div>
      <div className={styles.knowledgeRight} data-aos="fade-left">
        <p>
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
          nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor.
          <br />
          <br />
          Reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <button className={`btn ${styles.button}`}>FREE EVALUATION</button>
      </div>
    </div>
  );
}

export default Knowledge;
