import React, {useContext} from "react";
import styles from "./Testimonial.module.css";
import testimonialMain from "../../assets/main-home-testimonials-img-1.jpg";
import testimonialStarts from "../../assets/new-testimonials-stars.png";
// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react";
import { AppContext } from '../../context/AppContext';

// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";

// import required modules
import { Autoplay, Pagination } from "swiper/modules";

function Testimonial() {
  const {testimonalData } = useContext(AppContext);

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
