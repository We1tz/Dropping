import $api from "../http";

export default class VictorineService {
    static async Sendres(username, res, type){
        return $api.post('/sendvect', { username, res, type });
    }

    static async Getres(lower, upper){
        return $api.get('/getvect', { lower, upper });
    }
}