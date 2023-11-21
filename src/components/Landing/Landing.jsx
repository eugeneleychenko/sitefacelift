import React from 'react';
import { Parallax } from 'react-parallax';
import { Typography, Box } from '@mui/material';

const backgroundImage = 'https://images.unsplash.com/photo-1541421033552-fc06dba2ecd1?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&h=1500&w=2000&fit=clip&fm=jpg';

const Landing = () => {
  return (
    <Parallax bgImage={backgroundImage} strength={500}>
      <Box style={{ height: 500 }}>
        <Typography variant="h2" align="left">
          Site Refresh
        </Typography>
        <Typography variant="h3">
          Is your website lacking that "wow" factor? Look no further!
        </Typography>
        <Typography variant="h1">
          Elevate Your Website with Stunning Design
        </Typography>
        <Typography variant="h2">
          Our Approach: Creative Excellence
        </Typography>
        <Typography variant="h4">
          At Site Refresh, we believe that design should be jaw-droppingly beautiful. Our team of expert designers and developers will work closely with you to create a unique and visually stunning website that captures your brand's essence.
        </Typography>
        {/* ... Other content ... */}
      </Box>
    </Parallax>
  );
};

export default Landing;
