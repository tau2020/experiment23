import React from 'react';
import { useBilling } from '../hooks/useBilling';

const BillingHistory = () => {
    const { billingHistory } = useBilling();

    return (
        <div className='billing-history'>
            <h2>Billing History</h2>
            <ul>
                {billingHistory.map((bill, index) => (
                    <li key={index}>{bill.date}: ${bill.amount}</li>
                ))}
            </ul>
        </div>
    );
};

export default BillingHistory;
