import React, { FC, useContext, useState } from 'react';
import { Context } from "../../main";
import { observer } from "mobx-react-lite";
import { useNavigate } from 'react-router-dom';

function RestoreTemplate() {
    
    const [email, setEmail] = useState("")
    const [errors, setErrors] = useState([]);
    const { store } = useContext(Context);

""
    const validateValues = () => {
        setErrors([]);
        if (email.length < 4) {
            setErrors(["Название почты слишком короткое"]);
            return;
        }
        
        if (!email.includes("@") || !email.includes(".")){
            setErrors(["Неверно введена почта"]);
            return;
        }

        if(errors.length == 0){
            const g = store.restore(email).then(function(res){
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
                        <p></p>
                        <button type="button" class="btn btn-login-1 text-dark" onClick={() => { validateValues()}}>
                            Восстановить пароль
                        </button>
                    </div>
                    <ul>
                        {errors.map(i => {i})}
                    </ul>
                    </div>
            </form>
        </div>
  )
}

export default observer(RestoreTemplate);