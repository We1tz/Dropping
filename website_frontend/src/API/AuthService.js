import $api from "../http";

export default class AuthService {
    
    static async login(username, password){
        return $api.post('/login', { username, password });
    }

    static async registration(email, username, password){
        return $api.post('/register', { email, username, password });
    }

    static async repeatemail(email, username, password){
        return $api.post('/repeatemail', { email, username, password });
    }

    static async logout(){
        return $api.post('/logout');
    }

    static async restore(email, code){
        return $api.post('/restore', {email, code});
    }

    static async approve(email){
        return $api.post('/approve', {email});
    }
}