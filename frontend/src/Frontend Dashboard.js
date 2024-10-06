import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Dashboard.css';

const Dashboard = ({ auth_token }) => {
  const [patientRecords, setPatientRecords] = useState([]);
  const [appointments, setAppointments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const patientResponse = await axios.get('/api/patients', {
          headers: { Authorization: `Bearer ${auth_token}` }
        });
        const appointmentResponse = await axios.get('/api/appointments', {
          headers: { Authorization: `Bearer ${auth_token}` }
        });
        setPatientRecords(patientResponse.data);
        setAppointments(appointmentResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [auth_token]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <h2>Patient Records</h2>
      <ul>
        {patientRecords.map(record => (
          <li key={record.id}>{record.name}</li>
        ))}
      </ul>
      <h2>Appointments</h2>
      <ul>
        {appointments.map(appointment => (
          <li key={appointment.id}>{appointment.date} - {appointment.patientName}</li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;