import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

const App = ({ auth_token }) => {
  const [records, setRecords] = useState([]);
  const [appointments, setAppointments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const recordsResponse = await axios.get('/api/records', { headers: { Authorization: `Bearer ${auth_token}` } });
        const appointmentsResponse = await axios.get('/api/appointments', { headers: { Authorization: `Bearer ${auth_token}` } });
        setRecords(recordsResponse.data);
        setAppointments(appointmentsResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [auth_token]);

  const handleAppointmentCancel = async (id) => {
    try {
      await axios.delete(`/api/appointments/${id}`, { headers: { Authorization: `Bearer ${auth_token}` } });
      setAppointments(appointments.filter(appointment => appointment.id !== id));
    } catch (error) {
      console.error('Error cancelling appointment:', error);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div className="mobile-user-interface">
      <h1>Patient Records</h1>
      <ul>
        {records.map(record => (
          <li key={record.id}>{record.title}</li>
        ))}
      </ul>
      <h1>Appointments</h1>
      <ul>
        {appointments.map(appointment => (
          <li key={appointment.id}>
            {appointment.date} - {appointment.time} 
            <button onClick={() => handleAppointmentCancel(appointment.id)}>Cancel</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;