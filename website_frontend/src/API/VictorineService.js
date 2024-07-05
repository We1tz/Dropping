import $api from "../http";

export default class VictorineService {
    static async Sendres(res, type){
        return $api.post('/sendvect', { res, type });
    }

    static async Getres(email){
        return $api.get('/getvect', { email });
    }
}