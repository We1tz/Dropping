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
          setErrors([...errors,"Название почты слишком короткое"]);
        }
        if (password.length < 5) {
            setErrors([...errors, "Минимальная длина пароля - 5 символов"]);
        }
        if(password.match(signs)){
            setErrors([...errors,"Пароль должен содержать специальные знаки"]);
        }

        if(!errors){
            try{
                store.login(email, password);
            }
            catch(e){
                setErrors([...errors,"неверный логин или пароль"]);
            }
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
                        <button type="button" class="btn btn-login-1 " onClick={() => {setErrors([]); validateValues()}}>
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