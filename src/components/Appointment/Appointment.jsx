import React from "react";
import styles from "./Appointment.module.css";
import startImg from "../../assets/new-testimonials-stars.png";
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
      <p>Call us +012 34 56 789 or get your first consultation FREE!</p>
      <button className="btn">REQUEST APPOITMENT</button>
    </div>
  );
}

export default Appointment;
