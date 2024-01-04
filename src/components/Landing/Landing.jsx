import React, { useState, useEffect } from "react";
import styles from "./Landing.module.css";

const Landing = () => {
  const [text, setText] = useState("");
  const [isDeleting, setIsDeleting] = useState(false);
  const [fontIndex, setFontIndex] = useState(0);
  const fullText = "Site Refresh";
  const fonts = [
    "Pacifico",
    "Lobster",
    "Satisfy",
    "Permanent Marker",
    "Bangers",
    "Press Start 2P",
    "Indie Flower",
    "Shadows Into Light",
    "Amatic SC",
    "Dancing Script",
  ];
  const [colorIndex, setColorIndex] = useState(0);
  const colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    // ... more colors
  ];

  useEffect(() => {
    const handleTyping = () => {
      let currentText = isDeleting
        ? fullText.slice(0, text.length - 1)
        : fullText.slice(0, text.length + 1);
      setText(currentText);

      if (!isDeleting && currentText === fullText) {
        setTimeout(() => setIsDeleting(true), 2000);
      } else if (isDeleting && currentText === "") {
        setIsDeleting(false);
        setFontIndex((prevFontIndex) => (prevFontIndex + 1) % fonts.length);
      }

      if (isDeleting && currentText === "") {
        setColorIndex((prevColorIndex) => (prevColorIndex + 1) % colors.length);
      }
    };

    // const typingSpeed = Math.max(100, isDeleting ? 50 : 20);
    // Increase the typing speeds
    const typingSpeed = Math.max(50, isDeleting ? 25 : 10);
    const typingEffect = setTimeout(handleTyping, typingSpeed);

    return () => clearTimeout(typingEffect);
  }, [text, isDeleting, fonts.length]);

  return (
    <div
      className={styles.animatedText}
      style={{
        color: colors[colorIndex],
        background: "black",
        fontSize: "2rem",
        padding: "1rem",
        textAlign: "center",
        fontFamily: fonts[fontIndex], // Apply the current font
        height: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontSize: "128px",
      }}
    >
      {text}
    </div>
  );
};

export default Landing;
