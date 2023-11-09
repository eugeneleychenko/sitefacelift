import React from "react";
import styles from "./Testimonial.module.css";
import testimonialMain from "../../assets/main-home-testimonials-img-1.jpg";
import testimonialStarts from "../../assets/new-testimonials-stars.png";
// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react";

// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";

// import required modules
import { Autoplay, Pagination } from "swiper/modules";
const testimonalData = [
  {
    text: `"Tempus urna et pharetra pharetra massa. Iaculis urna id volutpat lacus. Lacus laoreet non curabitur gravida arcu ac tortor."`,
    author: "Daniel Taylor",
    profesation: "Co Founder",
  },
  {
    text: `"Turpis egestas pretium aenean pharetra magna ac placerat vestibulum lectus. Orci ac auctor augue mauris augue."`,
    author: "Susan Ward",
    profesation: "Judge",
  },
  {
    text: `"Fringilla est ullamcorper eget nulla facilisi etiam dignissim diam. Blandit turpis cursus in hac.Duis aute irure dolor in reprehenderit in."`,
    author: "Joseph Terry,",
    profesation: "Paralegal",
  },
];
function Testimonial() {
  return (
    <div className={styles.testimonial}>
      <div className={styles.testimonialLeft}>
        <img src={testimonialMain} alt="Testimonal main" />
      </div>
      <Swiper
        pagination={true}
        modules={[Autoplay, Pagination]}
        loop={true}
        autoplay={{
          delay: 40000,
          disableOnInteraction: false,
        }}
        className={styles.testimonialRight}
      >
        {testimonalData.map((item, index) => (
          <SwiperSlide key={index}>
            <div className={styles.content}>
              <img src={testimonialStarts} alt="" />
              <h1>{item.text}</h1>
              <h3>
                by {item.author}, {item.profesation}
              </h3>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
}

export default Testimonial;
