import React from "react";
import styles from "./Members.module.css";
import member1 from "../../assets/member-1.jpg";
import member2 from "../../assets/member-2.jpg";
import member3 from "../../assets/member-3.jpg";
import member4 from "../../assets/member-4.jpg";
import { BiLogoFacebook, BiLogoTwitter, BiLogoLinkedin } from "react-icons/bi";
const members = [
  {
    name: "Walter Hankins",
    img: member1,
    position: "Junior Partner",
    facebook: "/",
    linkedin: "/",
    twitter: "/",
  },
  {
    name: "Jenny Kang",
    img: member2,
    position: "Attorney",
    facebook: "/",
    linkedin: "/",
    twitter: "/",
  },
  {
    name: "Kent Bracamonte",
    img: member3,
    position: "Legal assistant",
    facebook: "/",
    linkedin: "/",
    twitter: "/",
  },
  {
    name: "Crystal Deane",
    img: member4,
    position: "Court clerk",
    facebook: "/",
    linkedin: "/",
    twitter: "/",
  },
];
function Members() {
  return (
    <div className={styles.members}>
      {members.map((item, index) => (
        <div className={styles.card} key={index}>
          <img src={item.img} alt={item.name} />
          <div className={styles.cardContentDiv}>
            <div className={styles.cardContent}>
              <h2>{item.name}</h2>
              <p>{item.position}</p>
              <div className={styles.social}>
                <a href={item.facebook} target="_blank" rel="noreferrer">
                  <BiLogoFacebook />
                </a>
                <a href={item.linkedin} target="_blank" rel="noreferrer">
                  <BiLogoLinkedin />
                </a>
                <a href={item.twitter} target="_blank" rel="noreferrer">
                  <BiLogoTwitter />
                </a>
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Members;
