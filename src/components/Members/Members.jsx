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
    img: member1,
    position: "Principal Attorney",
  },
  {
    name: "Stefanie Behler Soriano, Esq.",
    img: member2,
    position: "Associate Attorney",
  },
  {
    name: "Brian Robinson, Esq.",
    img: member3,
    position: "Of Counsel",

  },
  {
    name: "Toni Marie Angeli, Esq.",
    img: member4,
    position: "Of Counsel"
  }
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
              
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Members;
