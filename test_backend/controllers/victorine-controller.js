import victorineService from "../service/victorine-service";

class VictorineController {

    async Getresses(req, res, next){
        try{
            const {username, score, time} = req.body;
            return res.json(victorineService.getVictorine(username, score, time));
        }catch(e){
            next(e);
        }
    }
    async Givereses(req, res, next){
        try{
            const {ammount} = req.body;
            return res.json(victorineService.giveVictorine(ammount));
        }catch(e){
            next(e);
        }
    }
}

module.exports = new VictorineController();