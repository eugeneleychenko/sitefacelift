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
    text: `"Carmen was absolutely wonderful to work with. He was truly honest and I never felt taken advantage of. I can't recommend this law office and Carmen enough."`,
    author: "Jaime Oliver",
    location: "New York",
  },
  {
    text: `"Even after the case we still keep in contact for any question that we still might have, for people who do not speak English I recommend him, he makes sure that the person in the case understands everything that happens in their case."`,
    author: "Atriz R",
    location: "Manhattan, New York",
  },
  {
    text: `"When you go to their office you feel like you are home, they treat you like family, with empathy and professionalism; They are simply the best! I totally recommend this law firm. If you need reliable, experienced, and professional representation in your case, this is the right place to come, Giordano Law offices!"`,
    author: "Jesus Antonio M.",
    location: "Bronx, New York",
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
                by {item.author}, {item.location}
              </h3>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
}

export default Testimonial;
