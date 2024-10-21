import React from 'react';
import UserInfo from './UserInfo';
import BillingHistory from './BillingHistory';
import './Dashboard.css';

const Dashboard = () => {
    return (
        <div className='dashboard'>
            <h1>User Dashboard</h1>
            <UserInfo />
            <BillingHistory />
        </div>
    );
};

export default Dashboard;
