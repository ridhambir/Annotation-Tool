import React from 'react';
import { motion } from 'framer-motion';

const LeafAnimation = () => {
  const leafImages = [
    '/images/leaf1.svg',
    '/images/leaf2.svg',
    '/images/leaf3.svg',
    '/images/leaf4.svg',
    '/images/leaf5.svg',
  ];

  const leafVariants = {
    animate: {
      y: [0, window.innerHeight + 100],
      x: [0, 150, -100, 75, 0],
      rotate: [0, 720],
      opacity: [1, 0.5, 0],
    },
  };

  const leaves = Array.from({ length: 150 }, (_, i) => ({
    id: i,
    left: Math.random() * 100,
    delay: Math.random() * 5,
    duration: 50 + Math.random() * 40,
    size: 20 + Math.random() * 25,
    image: leafImages[Math.floor(Math.random() * leafImages.length)],
  }));

  return (
    <div className="leaf-container">
      {leaves.map((leaf) => (
        <motion.div
          key={leaf.id}
          className="leaf"
          variants={leafVariants}
          animate="animate"
          transition={{
            duration: leaf.duration,
            delay: leaf.delay,
            repeat: Infinity,
            repeatType: 'loop',
            ease: 'easeInOut',
          }}
          style={{
            left: `${leaf.left}%`,
            width: leaf.size,
            height: leaf.size,
            backgroundImage: `url(${leaf.image})`,
            backgroundSize: 'contain',
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center',
          }}
        />
      ))}
    </div>
  );
};

export default LeafAnimation;
