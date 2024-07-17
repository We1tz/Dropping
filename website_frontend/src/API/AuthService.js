import $api from "../http";

export default class AuthService {
    
    static async login(username, password){
        return $api.post('/login', { username, password });
    }

    static async registration(email, username, password){
        return $api.post('/register', { email, username, password });
    }

    static async logout(){
        return $api.post('/logout');
    }

    static async restore(code){
        return $api.post('/restore', {code});
    }

    static async approve(email){
        return $api.post('/approve', {email});
    }
}