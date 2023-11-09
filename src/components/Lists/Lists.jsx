import React from "react";
import styles from "./Lists.module.css";
import { Link } from "react-router-dom";
function Lists() {
  return (
    <div className={styles.lists}>
      <div>
        <span>01</span>
        <Link>
          {" "}
          <h1>Competition And Antitrust</h1>
        </Link>
      </div>
      <div>
        <span>02</span>
        <Link>
          {" "}
          <h1>Real Estate Law Firms</h1>
        </Link>
      </div>
      <div>
        <span>03</span>
        <Link>
          {" "}
          <h1>Marriage Contract</h1>
        </Link>
      </div>
      <div>
        <span>04</span>
        <Link>
          {" "}
          <h1>Legal Professional Law</h1>
        </Link>
      </div>
      <div>
        <span>05</span>
        <Link>
          {" "}
          <h1>Law & Justice</h1>
        </Link>
      </div>
      <div>
        <span>06</span>
        <Link>
          {" "}
          <h1>International Law & Justice</h1>
        </Link>
      </div>
    </div>
  );
}

export default Lists;
