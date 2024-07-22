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

    
    const [crrdate, setCrrdate] = useState(Date.now());
    const [cnt, setCnt] = useState(0);
    const [first, setFirst] = useState(false);

    const redirect = useNavigate();
    const approve = () =>{
        const g = AuthService.restore(email, code).then(function(res){
                if (res == "nope")
                {
                    console.log("ahegao");
                    setErrors(["неверный логин или пароль"]);
                    return;
                }
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
            setFirst(true);
            
            const g = store.approve(email);
            setIsApprActive(true);
        }
        console.log(errors)
        return errors;
    };
    const handlerepeatemail = () => {
        console.log(30000 + (crrdate-Date.now()));
        if(crrdate-Date.now() < -30000){
            store.approve(email)
            setCrrdate(Date.now());
            setCnt(cnt+1);
        }else {
            if ((30000 + (crrdate-Date.now())) > 0){
                if(String(30000 + (crrdate-Date.now())).length == 5)    {
                    setErrors(["Подождите " +String(30000 + (crrdate-Date.now())).substring(0, 2)+" секунд"]);
                }
                else{
                    setErrors(["Подождите " +String(30000 + (crrdate-Date.now())).substring(0, 1)+" секунд"]);
                }
                
            }
        }
        return;
    };
  return (
    <div>
            <form>
                    <div align="center" class="row">
                        <h1>Восстановление</h1>
                        
                    
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
                            <>
                            <button type="button" class="btn btn-login-1 text-dark" onClick={() => { approve()}}>
                                Подтвердить почту
                            </button>
                            
                            </>
                            :
                            <>
                            <button type="button" class="btn btn-login-1 text-dark" onClick={() => { validateValues()}}>
                                Восстановить пароль
                            </button>
                                
                            </>
                            
                        }
                    </div>
                    <ul>
                        {errors.map(i => <li>{i}</li>)}
                    </ul>
                    </div>
            </form>
            {isApprActive ? 
            <button className='btn btn-info' onClick={()=>{handlerepeatemail();}}>Прислать еще раз</button>: ""}
        </div>
  )
}

export default observer(RestoreTemplate);