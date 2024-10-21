import { useState, useEffect } from 'react';

export const useUser = () => {
    const [user, setUser] = useState({});

    useEffect(() => {
        // Fetch user data from API
        fetch('/api/user')
            .then(response => response.json())
            .then(data => setUser(data));
    }, []);

    return { user };
};
