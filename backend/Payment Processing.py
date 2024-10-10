from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Mock payment gateway function
def process_payment(payment_info):
    time.sleep(2)  # Simulate payment processing time
    return {'status': 'success', 'receipt': 'receipt12345'}

@app.route('/api/payment', methods=['POST'])
def payment_processing():
    data = request.json
    user_id = data.get('user_id')
    payment_info = data.get('payment_info')
    eBook_id = data.get('eBook_id')

    # Here you would typically authenticate the user and check eBook availability
    transaction_result = process_payment(payment_info)
    transaction_status = transaction_result['status']
    receipt = transaction_result['receipt']

    return jsonify({'transaction_status': transaction_status, 'receipt': receipt})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend code (React.js)
import React, { useState } from 'react';
import axios from 'axios';

const PaymentProcessing = () => {
    const [userId, setUserId] = useState('');
    const [paymentInfo, setPaymentInfo] = useState('');
    const [eBookId, setEBookId] = useState('');
    const [transactionStatus, setTransactionStatus] = useState('');
    const [receipt, setReceipt] = useState('');

    const handlePayment = async () => {
        const response = await axios.post('/api/payment', {
            user_id: userId,
            payment_info: paymentInfo,
            eBook_id: eBookId
        });
        setTransactionStatus(response.data.transaction_status);
        setReceipt(response.data.receipt);
    };

    return (
        <div>
            <h1>Payment Processing</h1>
            <input type='text' placeholder='User ID' onChange={(e) => setUserId(e.target.value)} />
            <input type='text' placeholder='Payment Info' onChange={(e) => setPaymentInfo(e.target.value)} />
            <input type='text' placeholder='eBook ID' onChange={(e) => setEBookId(e.target.value)} />
            <button onClick={handlePayment}>Pay</button>
            <div>Status: {transactionStatus}</div>
            <div>Receipt: {receipt}</div>
        </div>
    );
};

export default PaymentProcessing;