import React from "react";
import styles from "./Appointment.module.css";
import startImg from "../../assets/new-testimonials-stars.png";

const paragraph = "Call or text (646) 217-0749 to get a free consultation";


function Appointment() {
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
      <p>{paragraph}</p>
      <button className="btn">REQUEST APPOINTMENT</button>
    </div>
  );
}

export default Appointment;
