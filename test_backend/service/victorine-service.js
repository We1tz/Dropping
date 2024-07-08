const Vicresmodel = require('./models/vicres-model');

class VicresService {
    async getVicres(username, score, time) {
        const prevs = Vicresmodel.find({username});
        if (!prevs){
            const result = Vicresmodel.create({username, score, time});
            return result;
        }
        for (let i = 0; i < prevs.length; i++){
            if (prevs[i].score > score){
                return;
            }
        }
        const result = Vicresmodel.create({username, score, time});
        return result;
    }

    async getVicres(ammount){
        const result = Vicresmodel.find().sort({score: -1}).limit(ammount);
        return result;
    }
}

module.exports = new VicresService();