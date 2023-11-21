import React, { useState, useContext } from "react";
import styles from "./Header.module.css";
import Nav from "../Nav/Nav";
import { CiMenuFries } from "react-icons/ci";
import { BiSearch } from "react-icons/bi";
import { RxCross2 } from "react-icons/rx";
import { Link } from "react-router-dom";
import { AppContext } from '../../context/AppContext';


const Header = () => {
  const {linkNames} = useContext(AppContext);
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
        <ul className={styles.menuItems} style={{ gap: `${5700 / linkNames.join('').length}px` }}>
          {linkNames.map((item, index) => (
            <li key={index}>
              <Link>{item}</Link>
            </li>
          ))}
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
            {linkNames.map((name, index) => (
              <li key={index}>
                <Link>{name}</Link>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Header;

