import React, { useContext } from "react";
import styles from "./HeroSection.module.css";
// import signature from "../../assets/slider-signature.png";
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
import { AppContext } from "../../context/AppContext";

function HeroSection({ barHeight }) {
  const { companyName, subHeading } = useContext(AppContext);
  return (
    <div className={styles.heroSection}>
      <Header barHeight={barHeight} />
      <Swiper
        spaceBetween={30}
        effect={"fade"}
        loop={true}
        // navigation={false}
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
            <h1>{companyName}</h1>
            {subHeading !== "N/A" && subHeading !== "null" && (
              <h2>{subHeading}</h2>
            )}
            {/* <img src={signature} alt="Slider Signature" /> */}
          </div>
        </SwiperSlide>
        <SwiperSlide className={styles.slide}>
          <img src={slide2} alt="Slider 2" className={styles.sliderImage} />
          <div className={styles.sliderContent}>
            <h1 data-aos="fade-up">{companyName}</h1>
            {/* <img src={signature} alt="Slider Signature" /> */}
            {subHeading !== "N/A" && subHeading !== "null" && (
              <h2 data-aos="fade-up">{subHeading}</h2>
            )}
          </div>
        </SwiperSlide>
        <SwiperSlide className={styles.slide}>
          <img src={slide3} alt="Slider 3" className={styles.sliderImage} />
          <div className={styles.sliderContent}>
            <h1 data-aos="fade-up">{companyName}</h1>
            {subHeading !== "N/A" && subHeading !== "null" && (
              <h2 data-aos="fade-up">{subHeading}</h2>
            )}
            {/* <img src={signature} alt="Slider Signature" /> */}
          </div>
        </SwiperSlide>
      </Swiper>
    </div>
  );
}

export default HeroSection;
