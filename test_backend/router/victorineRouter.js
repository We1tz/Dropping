const Router = require('express').Router;
const VictorineController = require('../controllers/victorine-controller')
const Vicrouter = new Router();
const authMiddleware = require('../middlewares/auth-middleware');

Vicrouter.post('/post', authMiddleware, VictorineController.Getresses);
Vicrouter.get('/get', authMiddleware, VictorineController.Givereses);

module.exports = Vicrouter
