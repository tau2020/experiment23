import React from 'react';
import { useSelector } from 'react-redux';
import styles from './Skills.module.css';

const Skills = () => {
  const skills = useSelector(state => state.skills);

  return (
    <div className={styles.skills}>
      <h2>My Skills</h2>
      <ul>
        {skills.map(skill => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>
    </div>
  );
};

export default Skills;