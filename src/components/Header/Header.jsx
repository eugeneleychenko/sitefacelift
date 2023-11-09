import React, { useState } from "react";
import styles from "./Header.module.css";
import Nav from "../Nav/Nav";
import logo from "../../assets/new-logo-light.png";
import { CiMenuFries } from "react-icons/ci";
import { BiSearch } from "react-icons/bi";
import { RxCross2 } from "react-icons/rx";
import { Link } from "react-router-dom";
function Header() {
  const [isActive, setIsActive] = useState(false);
  return (
    <div className={styles.header}>
      <Nav />
      <hr />
      <div className={styles.headerStart}>
        <div className={styles.search}>
          <BiSearch />
          <div className={styles.searchElements}>
            <BiSearch />
            <input type="text" />
            <RxCross2 />
          </div>
        </div>
        <ul className={styles.menuItems}>
          <li>
            <Link> HOME</Link>
            <div className={styles.dropDown}>
              <ul>
                <li>
                  <Link>Main Home</Link>
                </li>
                <li>
                  <Link>Legal Advisory</Link>
                </li>
                <li>
                  <Link>Law Firm</Link>
                </li>
                <li>
                  <Link>Legal Consultant</Link>
                </li>
                <li>
                  <Link>Law Office</Link>
                </li>
                <li>
                  <Link>Interactive Links</Link>
                </li>
              </ul>
            </div>
          </li>
          <li>
            <Link> PAGES</Link>
            <div className={styles.dropDown}>
              <ul>
                <li>
                  <Link>Careers</Link>
                </li>
                <li>
                  <Link>FAQ Page</Link>
                </li>
                <li>
                  <Link>Contact Us</Link>
                </li>
                <li>
                  <Link>Get In Touch</Link>
                </li>
                <li>
                  <Link>Coming Soon</Link>
                </li>
              </ul>
            </div>
          </li>
          <li>
            <Link> PERSONNEL</Link>
            <div className={styles.dropDown}>
              <ul>
                <li>
                  <Link>Team Member</Link>
                </li>
                <li>
                  <Link>Our Team</Link>
                </li>
              </ul>
            </div>
          </li>
        </ul>
        <div className={styles.logo}>
          <img src={logo} alt="Website logo" />
        </div>
        <ul className={styles.menuItems}>
          <li>
            <Link>OUR EXPERTISE</Link>
          </li>
          <li>
            <Link>BLOG</Link>
          </li>
          <li>
            <Link>LANDING</Link>
          </li>
        </ul>
        <div
          className={styles.menu}
          onClick={() => {
            setIsActive(!isActive);
          }}
        >
          {isActive ? <RxCross2 /> : <CiMenuFries />}
        </div>

        <div
          className={`${styles.mobileMenu} ${isActive ? styles.active : ""}`}
        >
          <ul>
            <li>
              <Link> HOME</Link>
              <div className={styles.dropDown}>
                <ul>
                  <li>
                    <Link>Main Home</Link>
                  </li>
                  <li>
                    <Link>Legal Advisory</Link>
                  </li>
                  <li>
                    <Link>Law Firm</Link>
                  </li>
                  <li>
                    <Link>Legal Consultant</Link>
                  </li>
                  <li>
                    <Link>Law Office</Link>
                  </li>
                  <li>
                    <Link>Interactive Links</Link>
                  </li>
                </ul>
              </div>
            </li>
            <li>
              <Link> PAGES</Link>
              <div className={styles.dropDown}>
                <ul>
                  <li>
                    <Link>Careers</Link>
                  </li>
                  <li>
                    <Link>FAQ Page</Link>
                  </li>
                  <li>
                    <Link>Contact Us</Link>
                  </li>
                  <li>
                    <Link>Get In Touch</Link>
                  </li>
                  <li>
                    <Link>Coming Soon</Link>
                  </li>
                </ul>
              </div>
            </li>
            <li>
              <Link> PERSONNEL</Link>
              <div className={styles.dropDown}>
                <ul>
                  <li>
                    <Link>Team Member</Link>
                  </li>
                  <li>
                    <Link>Our Team</Link>
                  </li>
                </ul>
              </div>
            </li>
            <li>
              <Link>OUR EXPERTISE</Link>
            </li>
            <li>
              <Link>BLOG</Link>
            </li>
            <li>
              <Link>LANDING</Link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Header;
