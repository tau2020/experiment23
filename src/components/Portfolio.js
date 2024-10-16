import React from 'react';
import { useSelector } from 'react-redux';
import styles from './Portfolio.module.css';

const Portfolio = () => {
  const portfolioItems = useSelector(state => state.portfolio.items);

  return (
    <div className={styles.portfolio}>
      <h2>My Portfolio</h2>
      <div className={styles.items}>
        {portfolioItems.map(item => (
          <div key={item.id} className={styles.item}>
            <h3>{item.title}</h3>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Portfolio;