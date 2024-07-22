import AuthService from "../../API/AuthService";
import HomeFooter from "../awesome-components/footers/footer-home";
import BubbleTransition from "../awesome-components/transitions/bubble-transition";
import CurveTransition from "../awesome-components/transitions/curve-transition";
import HomeTemplate from "../awesome-templates/home-template";
import LoginForm from "../awesome-templates/login-template";
import { useState } from "react";

function ProfilePage() {

    const [prevpassword, setPrevpassword] = useState("")
    const [newpassword, setNewpassword] = useState("")
    const [confirmpassword, setConfirmPassword] = useState("")

    const [errors, setErrors] = useState([]);

    const [crrdate, setCrrdate] = useState(Date.now());
    const [cnt, setCnt] = useState(0);
    const [first, setFirst] = useState(false);

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
        if (newpassword.length < 8) {
            setErrors(["Минимальная длина пароля - 5 символов"]);
            return;
        }
        if(!newpassword.match(symbols)){
            setErrors(["Пароль должен содержать специальные знаки"]);
            return;
        }
        if(!newpassword.match(numbers)){
            setErrors(["Пароль должен содержать цифры"]);
            return;
        }
        if(!newpassword.match(upperCaseLetters)){
            setErrors(["Пароль должен содержать заглавные буквы"]);
            return;
        }
        if(!newpassword.match(lowerCaseLetters)){
            setErrors(["Пароль должен содержать строчные буквы"]);
            return;
        }
        if(newpassword != confirmpassword){
            setErrors(["пароль не совпадает с подтверждением пароля"]);
            return;
        }
        if ((30000 + (crrdate-Date.now())) > 0){
            if(String(30000 + (crrdate-Date.now())).length == 5)    {
                setErrors(["Подождите " + String(30000 + (crrdate-Date.now())).substring(0, 2) + " секунд"]);
                return
            }
            else{
                setErrors(["Подождите " + String(30000 + (crrdate-Date.now())).substring(0,1) +" секунд"]);
                return
            }
        }
        if(errors.length == 0){
            setCrrdate(Date.now());
            console.log((30000 + (crrdate-Date.now())));
            const g = AuthService.changepasswd(prevpassword, newpassword).then(function(res){
                if(res.data.status == "200"){
                    setCrrdate(Date.now());
                    setCnt(cnt+1);
                    redirect('/')
                    alert('Пароль успешно изменен');
                    return;
                }
                
                setCnt(cnt+1);
                setErrors(["Что-то пошло не так. Попробуйте снова."]);
                ;
            });
        }
        console.log(errors)
        return errors;
    };

    return (
        <div className="text-white">
            <HomeTemplate>
            
            <section class=" section-transition section-fullwindow">
            <div class="text-light login-jumbotron">
                <h1>Сменить пароль</h1>
                <form>
                    <div align="center" class="row">
                        
                    <div className='gap-3'>
                    <input
                        align="center"
                            class="form-control round-input"
                            onChange={e => setPrevpassword(e.target.value)}
                            value={prevpassword}
                            type="password"
                            placeholder='старый пароль'
                        />
                        <p></p>
                    <input
                        align="center"
                            class="form-control round-input"
                            onChange={e => setNewpassword(e.target.value)}
                            value={newpassword}
                            type="password"
                            placeholder='Новый пароль'
                        />
                        <p></p>
                    
                        <input
                            class="form-control round-input"
                            onChange={e => setConfirmPassword(e.target.value)}
                            value={confirmpassword}
                            type="password"
                            placeholder='Подтвердите пароль'
                        />
                        <p></p>
                        <br />
                        
                        <p></p>
                        
                    </div>
                    <ul>
                        {errors.map(i => <li>{i}</li>)}
                    </ul>
                        
                    </div>
            </form>
                        <button type="button" class="btn btn-login-1 text-dark" onClick={() => validateValues()}>
                            Сменить пароль
                        </button>
            </div>
            
            </section>
            </HomeTemplate>
            <HomeFooter />
            
        </div>
    );
}

export default ProfilePage;