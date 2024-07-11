import $api from "../http";

export default class AuthService {
    
    static async login(email, username, password){
        return $api.post('/login', { email, username, password });
    }

    static async registration(email, username, password){
        return $api.post('/register', { email, username, password });
    }

    static async logout(){
        return $api.post('/logout');
    }

    static async restore(email){
        return $api.post('/restore', {email});
    }
}