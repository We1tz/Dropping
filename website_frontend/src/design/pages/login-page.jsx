import HomeFooter from "../awesome-components/footers/footer-home";
import BubbleTransition from "../awesome-components/transitions/bubble-transition";
import CurveTransition from "../awesome-components/transitions/curve-transition";
import HomeTemplate from "../awesome-templates/home-template";
import LoginTemplate from "../awesome-templates/login-template";

function LoginFormPage() {
    return (
        <div className="text-white ">
            <HomeTemplate>
                <section class="section-transition section-fullwindow">
                    <div className="login-jumbotron text-light">
                        <img height="150" width="150" src="fox-logo.png" alt="" />
                        <h1 className="bold">Foxproof</h1>
                        
                        <LoginTemplate />
                    </div>
                </section>
            </HomeTemplate>
        </div>
    );
}

export default LoginFormPage;
