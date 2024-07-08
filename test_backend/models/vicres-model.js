const {Schema, model} = require('mongoose');

const VicresSchema = new Schema({
    user: {type: Schema.Types.ObjectId, ref: 'User'},
    time: {type: Date, required: true},
    score: {type: Number, required: true},
})

module.exports = model('Victorine Result', VicresSchema);