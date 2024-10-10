from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Mock database
users = {"user1": {"balance": 100}}
eBooks = {"ebook1": {"price": 10}}

@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json
    user_id = data.get('user_id')
    payment_info = data.get('payment_info')
    eBook_id = data.get('eBook_id')

    # Simulate transaction processing time
    time.sleep(2)  # Simulating a delay for processing

    # Check user balance and eBook price
    if user_id in users and eBook_id in eBooks:
        user_balance = users[user_id]['balance']
        eBook_price = eBooks[eBook_id]['price']

        if user_balance >= eBook_price:
            users[user_id]['balance'] -= eBook_price
            transaction_status = 'success'
            receipt = {"user_id": user_id, "eBook_id": eBook_id, "amount": eBook_price}
        else:
            transaction_status = 'failed'
            receipt = {"error": "Insufficient balance"}
    else:
        transaction_status = 'failed'
        receipt = {"error": "Invalid user or eBook"}

    return jsonify({"transaction_status": transaction_status, "receipt": receipt})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState } from 'react';

const PaymentProcessing = () => {
    const [userId, setUserId] = useState('');
    const [paymentInfo, setPaymentInfo] = useState('');
    const [eBookId, setEBookId] = useState('');
    const [transactionStatus, setTransactionStatus] = useState('');
    const [receipt, setReceipt] = useState(null);

    const handlePayment = async () => {
        const response = await fetch('http://localhost:5000/process_payment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, payment_info: paymentInfo, eBook_id: eBookId })
        });
        const data = await response.json();
        setTransactionStatus(data.transaction_status);
        setReceipt(data.receipt);
    };

    return (
        <div>
            <h1>Payment Processing</h1>
            <input type='text' placeholder='User ID' onChange={(e) => setUserId(e.target.value)} />
            <input type='text' placeholder='Payment Info' onChange={(e) => setPaymentInfo(e.target.value)} />
            <input type='text' placeholder='eBook ID' onChange={(e) => setEBookId(e.target.value)} />
            <button onClick={handlePayment}>Process Payment</button>
            <h2>Status: {transactionStatus}</h2>
            {receipt && <pre>{JSON.stringify(receipt, null, 2)}</pre>}
        </div>
    );
};

export default PaymentProcessing;