import React, { FC, useContext, useState } from 'react';
import { Context } from "../../main";
import { observer } from "mobx-react-lite";

function LoginTemplate() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

      const [errors, setErrors] = useState([]);
    const { store } = useContext(Context);

    const signs = "!@#$%^&*()_+=";
""
    const validateValues = () => {
        setErrors([]);
        if (email.length < 4) {
          setErrors(["Название почты слишком короткое"]);
          return
        }
        if (password.length < 5) {
            setErrors(["Минимальная длина пароля - 5 символов"]);
            return;
        }
        if(password.match(signs)){
            setErrors(["Пароль должен содержать специальные знаки"]);
            return;
        }
        if (!email.includes("@") || !email.includes(".")){
            setErrors(["Неверно введена почта"]);
            return;
        }

        if(errors.length == 0){
            const g = store.login(email, password).then(function(res){
                if(res == "nope"){
                    console.log("ahegao");
                    setErrors(["неверный логин или пароль"]);
                    return;
                }
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
                    <input
                        align="center"
                            class="form-control round-input"
                            onChange={e => setEmail(e.target.value)}
                            value={email}
                            type="email"
                            placeholder='Почта'
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
                        <button type="button" class="btn btn-login-1 " onClick={() => { validateValues()}}>
                            Войти
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

export default observer(LoginTemplate);