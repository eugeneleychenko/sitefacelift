import React from "react";
import styles from "./Nav.module.css";
import { Link } from "react-router-dom";
function Nav() {
  return (
    <nav className={styles.nav}>
      <div className={styles.navLeft}>
        <span>Monday to Friday 9:00 – 20:00</span> • {"  "}
        <a href="tel:00123456789">123.4567.8910</a>
      </div>
      <div className={styles.navRight}>
        <Link to={"#"}>Our Attorneys</Link>•<Link to={"#"}>FAQ</Link>•
        <Link to={"#"}>Practice Areas</Link>
      </div>
    </nav>
  );
}

export default Nav;
