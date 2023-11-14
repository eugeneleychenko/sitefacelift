import React from "react";
import styles from "./Members.module.css";
import member1 from "../../assets/member-1.jpg";
import member2 from "../../assets/member-2.jpg";
import member3 from "../../assets/member-3.jpg";
import member4 from "../../assets/member-4.jpg";
import { BiLogoFacebook, BiLogoTwitter, BiLogoLinkedin } from "react-icons/bi";
const members = [
  {
    name: "Carmen 'Jack' Giordano, Esq.",
    position: "Principal Attorney",
  },
  {
    name: "Stefanie Behler Soriano, Esq.",
    position: "Associate Attorney",
  },
  {
    name: "Brian Robinson, Esq.",
    position: "Of Counsel",
  },
  {
    name: "Toni Marie Angeli, Esq.",
    position: "Of Counsel"
  }
];
const memberImages = [member1, member2, member3, member4];
function Members() {
  return (
    <div className={styles.members}>
      {members.map((item, index) => (
        <div className={styles.card} key={index}>
          <img src={memberImages[index]} alt={item.name} />
          <div className={styles.cardContentDiv}>
            <div className={styles.cardContent}>
              <h2>{item.name}</h2>
              <p>{item.position}</p>
              
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Members;
