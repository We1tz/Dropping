import $api from "../http";

export default class VictorineService {
    static async Sendres(username, score, t){
        const type = t.toString();
        console.log({ score, t });
        return $api.post('/sendvect', { score, type });
    }

    /*
    Подходит Петька к Василиванычу и спрашивает 
    -Василиваныч что такое НЮАНС 
    Василивааныч и говорит 
    -снимай Петька штаны 
    Петька снял ...
    Василиваныч достает х.й и сует Петьке в жопу.. . 
    Вот смотри Петька у тебя х.й в жопе ...и у меня х.й в жопе. Но есть один нюанс!

    Вот именно этот нюанс возвращает промис, а не объект...
    */
    static async Getres(){
        return $api.get('/getvect');
    }
}