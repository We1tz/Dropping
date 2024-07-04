import HomeFooter from "../awesome-components/footers/footer-home";
import BubbleTransition from "../awesome-components/transitions/bubble-transition";
import CurveTransition from "../awesome-components/transitions/curve-transition";
import HomeTemplate from "../awesome-templates/home-template";
import RegisterTemplate from "../awesome-templates/register-template";

function RegisterFormPage() {
    return (
        <div className="text-white">
            <HomeTemplate>
                <section class="section-transition section-fullwindow">
                    <div className="login-jumbotron">
                        <img height="150" width="150" src="fox.png" alt="" />
                        <h1 className="bold">Foxproof</h1>
                        
                        <RegisterTemplate/>
                    </div>
                </section>
            </HomeTemplate>
        </div>
    );
}

export default RegisterFormPage;