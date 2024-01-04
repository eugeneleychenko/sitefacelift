// Landing.jsx

import React, { useEffect, useRef } from "react";
import gsap, { Power2, Power3 } from "gsap";
import styles from "./Landing.module.css"; // Assuming you've created a Landing.module.css file

const Landing = () => {
  const gridRef = useRef(null);

  useEffect(() => {
    const tl = gsap.timeline();
    tl.to(gridRef.current, { duration: 1, scaleY: 1.5, ease: Power3.easeIn })
      .to(gridRef.current, {
        duration: 1,
        rotationX: 75,
        y: "0%",
        ease: Power2.easeIn,
        transformPerspective: 300,
        onComplete: () => gridRef.current.classList.add(styles.isAnimating),
      })
      .to(gridRef.current.querySelector(`.${styles.logoWrap}`), {
        duration: 1,
        scale: 1,
      });
  }, []);

  return (
    <div className={styles.wrapper}>
      <div className={styles.grid} ref={gridRef}>
        <div className={styles.logo}>
          <div className={styles.logoWrap}>
            <h1>Site Refresh</h1>
            <div className={styles.subtitle}>
              Modernize. Optimize. Captivate.
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Landing;
