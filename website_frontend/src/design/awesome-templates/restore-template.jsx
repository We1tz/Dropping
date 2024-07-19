import React, { FC, useContext, useState } from 'react';
import { Context } from "../../main";
import { observer } from "mobx-react-lite";
import { useNavigate } from 'react-router-dom';
import AuthService from '../../API/AuthService';

function RestoreTemplate() {
    
    const [email, setEmail] = useState("");
    const [isApprActive, setIsApprActive] = useState(false);
    const [code, setCode] = useState("")
    const [errors, setErrors] = useState([]);
    const { store } = useContext(Context);
    const redirect = useNavigate();
    const approve = () =>{
        const g = AuthService.restore(email, code).then(function(res){
            if(res == "nope"){
                console.log("ahegao");
                setErrors(["неверный логин или пароль"]);
                return;
            }
            redirect("/login");
        });
    };
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
            const g = store.approve(email);
            setIsApprActive(true);
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
                        {
                            isApprActive ?
                            <>
                                <input
                                        align="center"
                                        class="form-control round-input"
                                        onChange={e => setCode(e.target.value)}
                                        value={code}
                                        type="email"
                                        placeholder='Код подтверждения'
                                    />
                                <p></p>
                                <p></p>
                            </>
                                :
                                <>
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
                                </>
                        }
                        {
                            isApprActive ?
                            <button type="button" class="btn btn-login-1 text-dark" onClick={() => { approve()}}>
                                Подтвердить почту
                            </button>
                            :
                            <button type="button" class="btn btn-login-1 text-dark" onClick={() => { validateValues()}}>
                                Восстановить пароль
                            </button>
                        }
                    </div>
                    <ul>
                        {errors.map(i => <li>{i}</li>)}
                    </ul>
                    </div>
            </form>
        </div>
  )
}

export default observer(RestoreTemplate);