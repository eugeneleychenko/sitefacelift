import React from "react";
import styles from "./BlogPosts.module.css";
import { Link } from "react-router-dom";
const blogData = [
  {
    title: "How Lawyer Can Help",
    date: "24.07.2023.",
    tags: ["FINANCES", "REAL ESTATE"],
    profession: "Co Founder Wendy",
    author: "Smith",
    link: "/",
  },
  {
    title: "Alternative Fee Arrangements",
    date: "24.07.2023.",
    tags: ["FINANCES", "REAL ESTATE"],
    profession: "Co Founder Wendy",
    author: "Smith",
    link: "/",
  },
  {
    title: "Becoming The Company",
    date: "24.07.2023.",
    tags: ["FINANCES", "REAL ESTATE", "REFERENCES"],
    profession: "Co Founder Wendy",
    author: "Smith",
    link: "/",
  },
  {
    title: "Business Skills All In",
    date: "24.07.2023.",
    tags: ["FINANCES", "REAL ESTATE"],
    profession: "Co Founder Wendy",
    author: "Smith",
    link: "/",
  },
];
function BlogPosts() {
  return (
    <div className={styles.blogPosts}>
      {blogData.map((item, index) => (
        <div>
          <div className={styles.item} key={index} data-aos="fade-up">
            <div>
              <div className={styles.top}>
                <div className={styles.date}>{item.date}</div>
                <div className={styles.tags}>
                  {item.tags.map((tag, index) => (
                    <span key={index}>
                      {tag}
                      <span>{index < item.tags.length - 1 && "•"}</span>
                    </span>
                  ))}
                </div>
              </div>
              <h1>{item.title}</h1>
            </div>
            <div className={styles.info}>
              <p>{item.profession}</p>
              <p>{item.author}</p>
            </div>
            <div>
              <Link to={item.link}>
                <button className="btn">View MORE</button>
              </Link>
            </div>
          </div>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default BlogPosts;
