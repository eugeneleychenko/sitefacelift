import React, { useContext } from "react";
import styles from "./Appointment.module.css";
import startImg from "../../assets/new-testimonials-stars.png";
import { AppContext } from "../../context/AppContext";

function Appointment() {
  const { paragraph } = useContext(AppContext);

  return (
    <div className={styles.appointment}>
      <img
        loading="lazy"
        width="186"
        height="28"
        src={startImg}
        alt="a"
        decoding="async"
      />
      <h1>The Right Approach To Your Legal Problem</h1>
      {paragraph && paragraph !== "N/A" && paragraph !== "null" && (
        <p>{paragraph}</p>
      )}
      <button className="btn">REQUEST APPOINTMENT</button>
    </div>
  );
}

export default Appointment;
