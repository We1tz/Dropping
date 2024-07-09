import $api from "../http";

export default class AnalitService {
    static async GetAllSuspisious(){
        return $api.get('/getsusps');
    }
    static async GetSuspisious(id){
        return $api.get('/getsusp', id);
    }
}