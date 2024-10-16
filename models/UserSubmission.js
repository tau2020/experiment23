const mongoose = require('mongoose');

const userSubmissionSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, required: true },
  submissionData: { type: Object, required: true },
  submittedAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('UserSubmission', userSubmissionSchema);