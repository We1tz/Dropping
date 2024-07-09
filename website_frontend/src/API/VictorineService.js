import $api from "../http";

export default class VictorineService {
    static async Sendres(username, score, t){
        const time = t.toString();
        console.log({ score, time });
        return $api.post('/sendvect', { score, time });
    }

    static async Getres(lower, upper){
        return $api.get('/getvect', { lower, upper });
    }
}