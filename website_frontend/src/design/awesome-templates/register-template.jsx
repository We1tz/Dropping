import React, { FC, useContext, useState } from 'react';
import { Context } from "../../main";
import { observer } from "mobx-react-lite";
import { useNavigate } from 'react-router-dom';

function RegisterTemplate() {

    const redirect = useNavigate();

    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const { store } = useContext(Context);

    const [errors, setErrors] = useState([]);
    const validateValues = () => {
        setErrors([]);
        /*
        if (email.length < 4) {
          setErrors(["Название почты слишком короткое"]);
          return;
        }
          */
        if (username.length < 4) {
            setErrors(["имя пользователя слишком короткое"]);
            return;
        }
        if (password.length < 5) {
            setErrors(["Минимальная длина пароля - 5 символов"]);
            return;
        }
        /*
        if (!email.includes("@") || !email.includes(".")){
            setErrors(["Неверно введена почта"]);
            return;
        }*/

        try{
            store.registration(username, password);
            redirect('/');
        }
        catch(e){
            console.log(e);
            setErrors(["неверный логин или пароль"]);
        }
        console.log(errors)
        return errors;
    };


    return (
        <div>
            <form>
                    <div align="center" class="row">
                        <h1>Регистрация</h1>
                        
                    <p></p>
                    <p></p>
                    
                    <div className='gap-3'>
                    <input
                        align="center"
                            class="form-control round-input"
                            onChange={e => setUsername(e.target.value)}
                            value={username}
                            type="text"
                            placeholder='Имя пользователя'
                        />
                        <p></p>
                        {/*
                        <input
                        align="center"
                            class="form-control round-input"
                            onChange={e => setEmail(e.target.value)}
                            value={email}
                            type="text"
                            placeholder='Имя пользователя'
                        />
                        */ }
                    
                        <input
                            class="form-control round-input"
                            onChange={e => setPassword(e.target.value)}
                            value={password}
                            type="password"
                            placeholder='Пароль'
                        />
                        <p></p>
                        Уже есть аккаунт? <a className="link-dark" href="/login">Войти</a>
                        <br />
                        <br />
                        <button type="button" class="btn btn-login-1 " onClick={() => validateValues()}>
                            Зарегистрироваться
                        </button>
                    </div>
                    <ul>
                        {errors.map(i => <li>{i}</li>)}
                    </ul>
                        
                    </div>
            </form>
        </div>
    );
}

export default observer(RegisterTemplate);