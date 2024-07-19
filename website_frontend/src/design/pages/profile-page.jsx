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

    const validateValues = () => {
        setErrors([]);
        console.log("jopa");
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
        if(errors.length == 0){
            const g = AuthService.changepasswd(prevpassword, newpassword).then(function(res){
                if(res.data.result == "200"){
                    redirect('/')
                    alert('Пароль успешно изменен');
                    return;
                }
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
            <div class="text-light grad-article login-jumbotron">
            <section class=" section-article section-fullwindow">
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
                        <button type="button" class="btn btn-login-1 text-dark" onClick={() => validateValues()}>
                            Сменить пароль
                        </button>
                        <p></p>
                        
                    </div>
                    <ul>
                        {errors.map(i => <li>{i}</li>)}
                    </ul>
                        
                    </div>
            </form>
            </section>
            </div>
            </HomeTemplate>
            <HomeFooter />
            
        </div>
    );
}

export default ProfilePage;