from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Mock database for users and cars
users = {1: 'User1', 2: 'User2'}
cars = {1: 'Car1', 2: 'Car2'}

@app.route('/process_payment', methods=['POST'])
def process_payment():
    start_time = time.time()
    data = request.json
    payment_details = data.get('paymentDetails')
    user_id = data.get('userId')
    car_id = data.get('carId')

    # Simulate payment processing
    if user_id not in users or car_id not in cars:
        return jsonify({'transactionStatus': 'failed', 'receipt': None}), 400

    # Simulate a successful transaction
    transaction_status = 'success'
    receipt = {'userId': user_id, 'carId': car_id, 'amount': payment_details['amount'], 'status': transaction_status}

    # Check processing time
    processing_time = time.time() - start_time
    if processing_time > 0.5:
        return jsonify({'transactionStatus': 'failed', 'receipt': None}), 500

    return jsonify({'transactionStatus': transaction_status, 'receipt': receipt})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend Code (React.js)
import React, { useState } from 'react';

const PaymentProcessing = () => {
    const [paymentDetails, setPaymentDetails] = useState({ amount: 0 });
    const [userId, setUserId] = useState(1);
    const [carId, setCarId] = useState(1);
    const [transactionStatus, setTransactionStatus] = useState('');
    const [receipt, setReceipt] = useState(null);

    const handlePayment = async () => {
        const response = await fetch('http://localhost:5000/process_payment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ paymentDetails, userId, carId })
        });
        const data = await response.json();
        setTransactionStatus(data.transactionStatus);
        setReceipt(data.receipt);
    };

    return (
        <div>
            <h1>Payment Processing</h1>
            <input type='number' value={paymentDetails.amount} onChange={(e) => setPaymentDetails({ amount: e.target.value })} placeholder='Amount' />
            <button onClick={handlePayment}>Process Payment</button>
            <div>Status: {transactionStatus}</div>
            {receipt && <div>Receipt: {JSON.stringify(receipt)}</div>}
        </div>
    );
};

export default PaymentProcessing;