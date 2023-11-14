import React from "react";
import styles from "./Nav.module.css";
import { Link } from "react-router-dom";

const openHours = "Monday to Friday: 10.00 AM – 8.00 PM"
const phoneNumber = "(646) 217-0749"
function Nav() {
  return (
    <nav className={styles.nav}>
      <div className={styles.navLeft}>
        <span>{openHours}</span> • {"  "}
        <a href={`tel:${phoneNumber}`}>{phoneNumber}</a>
      </div>
      <div className={styles.navRight}>
        <Link to={"#"}>Our Attorneys</Link>•<Link to={"#"}>FAQ</Link>•
        <Link to={"#"}>Practice Areas</Link>
      </div>
    </nav>
  );
}

export default Nav;
