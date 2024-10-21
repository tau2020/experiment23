import React from 'react';
import { useUser } from '../hooks/useUser';

const UserInfo = () => {
    const { user } = useUser();

    return (
        <div className='user-info'>
            <h2>User Information</h2>
            <p>Name: {user.name}</p>
            <p>Email: {user.email}</p>
        </div>
    );
};

export default UserInfo;
