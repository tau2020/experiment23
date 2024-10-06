from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Mock database
users = {1: 'User1', 2: 'User2'}
cars = {1: 'Car1', 2: 'Car2'}

@app.route('/process_payment', methods=['POST'])
def process_payment():
    start_time = time.time()
    data = request.json
    user_id = data.get('userId')
    car_id = data.get('carId')
    payment_details = data.get('paymentDetails')

    # Simulate payment processing
    if user_id in users and car_id in cars:
        # Here you would integrate with a payment gateway
        transaction_status = 'Success'
        receipt = {'transactionId': '12345', 'amount': payment_details['amount']}
    else:
        transaction_status = 'Failed'
        receipt = None

    processing_time = time.time() - start_time
    if processing_time > 0.5:
        return jsonify({'error': 'Processing time exceeded limit'}), 500

    return jsonify({'transactionStatus': transaction_status, 'receipt': receipt})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend Code (React)
import React, { useState } from 'react';

const PaymentProcessing = () => {
    const [userId, setUserId] = useState('');
    const [carId, setCarId] = useState('');
    const [amount, setAmount] = useState('');
    const [transactionStatus, setTransactionStatus] = useState('');
    const [receipt, setReceipt] = useState(null);

    const handlePayment = async () => {
        const response = await fetch('http://localhost:5000/process_payment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ userId, carId, paymentDetails: { amount } })
        });
        const data = await response.json();
        setTransactionStatus(data.transactionStatus);
        setReceipt(data.receipt);
    };

    return (
        <div>
            <h1>Payment Processing</h1>
            <input type='text' placeholder='User ID' value={userId} onChange={(e) => setUserId(e.target.value)} />
            <input type='text' placeholder='Car ID' value={carId} onChange={(e) => setCarId(e.target.value)} />
            <input type='text' placeholder='Amount' value={amount} onChange={(e) => setAmount(e.target.value)} />
            <button onClick={handlePayment}>Process Payment</button>
            <div>Status: {transactionStatus}</div>
            {receipt && <div>Receipt: {JSON.stringify(receipt)}</div>}
        </div>
    );
};

export default PaymentProcessing;