import React, {useContext} from "react";
import styles from "./Nav.module.css";
import { Link } from "react-router-dom";
import { AppContext } from '../../context/AppContext';



function Nav() {
  const { openHours, phoneNumber  } = useContext(AppContext);
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
