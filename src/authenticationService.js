const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const User = require('./models/User');

class AuthenticationService {
  constructor(secret, expiresIn) {
    this.secret = secret;
    this.expiresIn = expiresIn;
  }

  async register(userData) {
    const hashedPassword = await bcrypt.hash(userData.password, 10);
    const user = new User({
      username: userData.username,
      password: hashedPassword,
      role: userData.role || 'user'
    });
    return await user.save();
  }

  async login(username, password) {
    const user = await User.findOne({ username });
    if (!user) throw new Error('User not found');
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) throw new Error('Invalid credentials');
    const token = jwt.sign({ id: user._id, role: user.role }, this.secret, { expiresIn: this.expiresIn });
    return { token };
  }

  authenticateToken(req, res, next) {
    const token = req.headers['authorization'] && req.headers['authorization'].split(' ')[1];
    if (!token) return res.sendStatus(401);
    jwt.verify(token, this.secret, (err, user) => {
      if (err) return res.sendStatus(403);
      req.user = user;
      next();
    });
  }
}

module.exports = AuthenticationService;