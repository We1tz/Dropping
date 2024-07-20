import React, { FC, useContext, useState } from 'react';
import { Context } from "../../main";
import { observer } from "mobx-react-lite";
import { useNavigate } from 'react-router-dom';

function LoginTemplate() {

    const redirect = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

      const [errors, setErrors] = useState([]);
    const { store } = useContext(Context);

""
    const validateValues = () => {
        setErrors([]);
        console.log("J0P4");
        var lowerCaseLetters = /[a-z]/g;
        var upperCaseLetters = /[A-Z]/g;
        const symbols = /[^A-Za-z0-9]/g;
        const numbers = /[0-9]/g;
        /*
        if (email.length < 4) {
          setErrors(["Название почты слишком короткое"]);
          return
        }
          */
        if (password.length < 8) {
            setErrors(["Минимальная длина пароля - 5 символов"]);
            return;
        }
        if(!password.match(symbols)){
            setErrors(["Пароль должен содержать специальные знаки"]);
            return;
        }
        if(!password.match(numbers)){
            setErrors(["Пароль должен содержать цифры"]);
            return;
        }
        if(!password.match(upperCaseLetters)){
            setErrors(["Пароль должен содержать заглавные буквы"]);
            return;
        }
        if(!password.match(lowerCaseLetters)){
            setErrors(["Пароль должен содержать строчные буквы"]);
            return;
        }
        console.log("J0P4");
        if(errors.length == 0){
            const g = store.login(username, password).then(function(res){
                if(res == "nope"){
                    console.log("sadovnikov");
                    setErrors(["неверный логин или пароль"]);
                    return;
                }
                redirect('/');
            });
        }
        console.log(errors)
        return errors;
    };

    return (
        <div>
            <form>
                    <div align="center" class="row">
                        <h1>Вход</h1>
                        
                    
                    <div className='gap-3'>
                    {/*
                    <input
                        align="center"
                            class="form-control round-input"
                            onChange={e => setEmail(e.target.value)}
                            value={email}
                            type="email"
                            placeholder='Почта'
                        />
                        <p></p>
                        */}
                    <input
                        align="center"
                            class="form-control round-input"
                            onChange={e => setUsername(e.target.value)}
                            value={username}
                            type="text"
                            placeholder='Имя пользователя'
                        />
                        <p></p>
                        <input
                            class="form-control round-input"
                            onChange={e => setPassword(e.target.value)}
                            value={password}
                            type="password"
                            placeholder='Пароль'
                        />
                        <p></p>
                        <a className="link-light text-start" href="/restorepass">Забыли пароль?</a>
                        <br />
                        <br />
                        <button type="button" class="btn btn-login-1 text-dark" onClick={() => { validateValues()}}>
                            Войти
                        </button>
                        <br />
                    </div>
                    <ul>
                        {errors.map(i => <li>{i}</li>)}
                    </ul>
                    </div>
            </form>
        </div>
    );
}


export default observer(LoginTemplate);