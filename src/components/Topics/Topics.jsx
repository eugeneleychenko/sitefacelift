import React from "react";
import styles from "./Topics.module.css";
function Topics() {
  return (
    <div className={styles.topics}>
      <div data-aos="fade-right"  data-aos-anchor-placement="center-bottom">
        <img
          loading="lazy"
          width="400"
          height="605"
          src="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-1.jpg"
          class="attachment-full size-full"
          alt="a"
          decoding="async"
          srcset="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-1.jpg 400w, https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-1-198x300.jpg 198w"
          sizes="(max-width: 400px) 100vw, 400px"
        />
        <h4>CONSALTING</h4>
      </div>
      <div data-aos="fade-up" data-aos-anchor-placement="center-bottom">
        <img
          loading="lazy"
          width="300"
          height="450"
          src="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-2.jpg"
          class="attachment-full size-full"
          alt="a"
          decoding="async"
          srcset="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-2.jpg 300w, https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-2-200x300.jpg 200w"
          sizes="(max-width: 300px) 100vw, 300px"
        />
        <h4>HUMAN RIGHT</h4>
      </div>
      <div data-aos="fade-up" data-aos-anchor-placement="center-bottom">
        <img
          loading="lazy"
          width="700"
          height="466"
          src="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-3.jpg"
          class="attachment-full size-full"
          alt="a"
          decoding="async"
          srcset="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-3.jpg 700w, https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-3-300x200.jpg 300w, https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-3-600x399.jpg 600w"
          sizes="(max-width: 700px) 100vw, 700px"
        />
        <h4>INTELECTUAL PROPERTY</h4>
      </div>
      <div data-aos="fade-left">
        <img
          loading="lazy"
          width="400"
          height="572"
          src="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-4.jpg"
          class="attachment-full size-full"
          alt=""
          decoding="async"
          srcset="https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-4.jpg 400w, https://courtroom.qodeinteractive.com/wp-content/uploads/2023/07/img-with-text-4-210x300.jpg 210w"
          sizes="(max-width: 400px) 100vw, 400px"
        />
        <h4>COMPANY COMMERCIAL</h4>
      </div>
    </div>
  );
}

export default Topics;
