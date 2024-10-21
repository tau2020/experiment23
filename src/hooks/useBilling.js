import { useState, useEffect } from 'react';

export const useBilling = () => {
    const [billingHistory, setBillingHistory] = useState([]);

    useEffect(() => {
        // Fetch billing history from API
        fetch('/api/billing')
            .then(response => response.json())
            .then(data => setBillingHistory(data));
    }, []);

    return { billingHistory };
};
