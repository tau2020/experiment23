import React, { useState } from 'react';
import axios from 'axios';
import styles from './ContactForm.module.css';

const ContactForm = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/api/contact', { name, email, message });
      setStatus('Message sent!');
    } catch (error) {
      setStatus('Error sending message.');
    }
  };

  return (
    <form className={styles.contactForm} onSubmit={handleSubmit}>
      <h2>Contact Me</h2>
      <input type='text' placeholder='Name' value={name} onChange={(e) => setName(e.target.value)} required />
      <input type='email' placeholder='Email' value={email} onChange={(e) => setEmail(e.target.value)} required />
      <textarea placeholder='Message' value={message} onChange={(e) => setMessage(e.target.value)} required></textarea>
      <button type='submit'>Send</button>
      {status && <p>{status}</p>}
    </form>
  );
};

export default ContactForm;