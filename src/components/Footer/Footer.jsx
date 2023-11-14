import React, { useContext } from "react";
import styles from "./Footer.module.css";
import logo from "../../assets/new-logo-gold.png";
import { BiLogoFacebook, BiLogoTwitter, BiLogoLinkedin } from "react-icons/bi";
import { Link } from "react-router-dom";
import { AppContext } from '../../context/AppContext';



function Footer() {

  const {address, phoneNumber, email} = useContext(AppContext);
  return (
    <footer className={styles.footer}>
      <div>
        {/* <img src={logo} alt="Logo" />
        <p>
          Lorem ipsum dolor sit amet, consectetur scing elit, sed do eiusmod
          tempor incididu! Nut ut labore et dolore magna aliqua.
        </p> */}
        <div className={styles.social}>
          <a href="/" target="_blank" rel="noreferrer">
            <BiLogoFacebook />
          </a>
          <a href="/" target="_blank" rel="noreferrer">
            <BiLogoLinkedin />
          </a>
          <a href="/" target="_blank" rel="noreferrer">
            <BiLogoTwitter />
          </a>
        </div>
      </div>
      <div>
        <h1>Links</h1>
        <ul className={styles.links}>
          <li>
            <Link to={"/"}>OUR TEAM</Link>
          </li>
          <li>
            <Link to={"/"}>TEAM MEMBER</Link>
          </li>
          <li>
            <Link to={"/"}>GET IN TOUCH</Link>
          </li>
          <li>
            <Link to={"/"}>CONTACT US</Link>
          </li>
          <li>
            <Link to={"/"}>ABOUT US</Link>
          </li>
        </ul>
      </div>
      <div>
        <h1>Find </h1>
        <p>
          <a
            rel="noreferrer noopener"
            href="https://www.google.com/maps/place/35+Ridge+St,+New+York,+NY+10002,+USA/@40.7165617,-73.9867446,17z/data=!3m1!4b1!4m5!3m4!1s0x89c25980135e5fff:0x1200dbe5ac7a800!8m2!3d40.7165577!4d-73.9845559?_ga=2.94611102.304902709.1697972977-111006533.1697636651"
            target="_blank"
          >
            {address}
          </a>
        </p>

        <p>
          <a href={`tel:${phoneNumber}`}>{phoneNumber}</a>
        </p>
        <p>
          <a href={`mailto:${email}`}>{email}</a>
        </p>
      </div>
      <div>
        <h1>Questions</h1>
        <p>
          <a class="qodef--underline-link" href="/faq">
            Do I Need A Personal Lawyer?
          </a>
        </p>
        <p>
          <a class="qodef--underline-link" href="/faq">
            How Can We Help You?
          </a>
        </p>
        <p>
          <a class="qodef--underline-link" href="/faq">
            What Is Domestic Violence?
          </a>
        </p>
        <p>
          <a class="qodef--underline-link" href="/faq/">
            Are You Licensed In My Country?
          </a>
        </p>
        <p>
          <a
            class="qodef--underline-link"
            href="https://courtroom.qodeinteractive.com/faq/"
          >
            How Do I Choose a Lawyer?
          </a>
        </p>
      </div>
    </footer>
  );
}

export default Footer;
