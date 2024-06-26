import React, { useContext } from "react";
import styles from "./Members.module.css";
import member1 from "../../assets/member-1.jpg";
import member2 from "../../assets/member-2.jpg";
import member3 from "../../assets/member-3.jpg";
import member4 from "../../assets/member-4.jpg";
import { BiLogoFacebook, BiLogoTwitter, BiLogoLinkedin } from "react-icons/bi";
import { AppContext } from "../../context/AppContext";

function Members() {
  const { members } = useContext(AppContext);

  if (!Array.isArray(members)) {
    // Handle the case where members is not an array
    return null;
  }

  const memberImages = [member1, member2, member3, member4];

  return (
    <div className={styles.members}>
      {members.map((item, index) => {
        const position =
          item.position && item.position.toLowerCase() !== "null"
            ? item.position
            : "Attorney";
        if (position.toLowerCase() === "n/a") {
          return null;
        }
        return (
          <div className={styles.card} key={index}>
            <img src={memberImages[index]} alt={item.name} />
            <div className={styles.cardContentDiv}>
              <div className={styles.cardContent}>
                <h2>{item.name}</h2>
                {position && <p>{position}</p>}
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default Members;
