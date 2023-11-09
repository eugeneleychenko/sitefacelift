import React from "react";
import styles from "./HeroSection.module.css";
import signature from "../../assets/slider-signature.png";
import slide1 from "../../assets/slider-1.jpg";
import slide2 from "../../assets/slider-2.jpg";
import slide3 from "../../assets/slider-3.jpg";
// Import Swiper React components
import { Swiper, SwiperSlide } from "swiper/react";
// Import Swiper styles
import "swiper/css";
import "swiper/css/effect-fade";
import "swiper/css/navigation";
import "swiper/css/pagination";
// import required modules
import { Autoplay, EffectFade, Navigation, Pagination } from "swiper/modules";
import Header from "../Header/Header";

function HeroSection() {
  return (
    <div className={styles.heroSection}>
      <Header />
      <Swiper
        spaceBetween={30}
        effect={"fade"}
        loop={true}
        navigation={true}
        pagination={{
          clickable: true,
        }}
        modules={[Autoplay, EffectFade, Navigation, Pagination]}
        className="mySwiper"
        fadeEffect={{
          crossFade: true,
          cssMode: true, // Enable CSS mode for smoother transitions
        }}
        speed={1000}
        autoplay={{
          delay: 4000,
          disableOnInteraction: false,
        }}
      >
        <SwiperSlide className={styles.slide}>
          <img src={slide1} alt="Slider 1" className={styles.sliderImage} />
          <div className={styles.sliderContent}>
            <h1>Legal Consultant</h1>
            <img src={signature} alt="Slider Signature" />
          </div>
        </SwiperSlide>
        <SwiperSlide className={styles.slide}>
          <img src={slide2} alt="Slider 2" className={styles.sliderImage} />
          <div className={styles.sliderContent}>
            <h1 data-aos="fade-up">Legal Consultant</h1>
            <img src={signature} alt="Slider Signature" />
          </div>
        </SwiperSlide>
        <SwiperSlide className={styles.slide}>
          <img src={slide3} alt="Slider 3" className={styles.sliderImage} />
          <div className={styles.sliderContent}>
            <h1 data-aos="fade-up">Legal Consultant</h1>
            <img src={signature} alt="Slider Signature" />
          </div>
        </SwiperSlide>
      </Swiper>
    </div>
  );
}

export default HeroSection;