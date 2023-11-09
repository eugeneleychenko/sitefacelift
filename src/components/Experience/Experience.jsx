import React from "react";
import styles from "./Experience.module.css";
import logo1 from "../../assets/client-png-1.png";
import logo2 from "../../assets/client-png-2.png";
import logo3 from "../../assets/client-new-x2.png";
import logo4 from "../../assets/client-new-x2-financial.png";
import logo5 from "../../assets/client-png-3.png";
import logo6 from "../../assets/client-png-4.png";
import logo7 from "../../assets/client-png-5.png";
import logo8 from "../../assets/client-png-6.png";
import { Link } from "react-router-dom";

function Experience() {
  return (
    <div className={styles.experience}>
      <div className={styles.experienceLeft}>
        <h1>
          Over 30 Years Experience,
          <br /> Qualified Legal Attorneys
        </h1>
      </div>
      <div className={styles.experienceRight}>
        <Link>
          <img src={logo1} alt="Logo" />
        </Link>
        <Link>
          <img src={logo3} alt="Logo" />
        </Link>
        <Link>
          <img src={logo2} alt="Logo" />
        </Link>
        <Link>
          <img src={logo4} alt="Logo" />
        </Link>
        <Link>
          <img src={logo5} alt="Logo" />
        </Link>
        <Link>
          <img src={logo6} alt="Logo" />
        </Link>
        <Link>
          <img src={logo7} alt="Logo" />
        </Link>
        <Link>
          <img src={logo8} alt="Logo" />
        </Link>
      </div>
    </div>
  );
}

export default Experience;
