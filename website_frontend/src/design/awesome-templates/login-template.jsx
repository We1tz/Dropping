import React, { FC, useContext, useState } from 'react';
import { Context } from "../../main";
import { observer } from "mobx-react-lite";

function LoginTemplate() {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const { store } = useContext(Context);

    return (
        <div>
            <form>
                    <div align="center" class="row">
                    <div class="btn-group" role="group" aria-label="Basic example">
                    <button type="button" class="btn btn-light sign-btn" onClick={() => store.login(email, password)}>
                            Войти
                        </button>
                        <button type="button" class="btn btn-login-1 sign-btn" onClick={() => store.registration(email, password)}>
                            Зарегистрироваться
                        </button>
                    </div>
                    <p></p>
                    <p></p>
                    
                    <div className='gap-3'>
                    <input
                        align="center"
                            class="form-control w-75 round-input"
                            onChange={e => setEmail(e.target.value)}
                            value={email}
                            type="text"
                            placeholder='Почта'
                        />
                        <p></p>
                        <input
                            class="form-control w-75 round-input"
                            onChange={e => setPassword(e.target.value)}
                            value={password}
                            type="password"
                            placeholder='Пароль'
                        />
                        <p></p>
                    </div>
                        
                        
                    </div>
            </form>
        </div>
    );
}

export default observer(LoginTemplate);