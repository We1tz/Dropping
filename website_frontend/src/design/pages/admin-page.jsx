import HomeFooter from "../awesome-components/footers/footer-home";
import BubbleTransition from "../awesome-components/transitions/bubble-transition";
import CurveTransition from "../awesome-components/transitions/curve-transition";
import HomeTemplate from "../awesome-templates/home-template";
import LoginForm from "../awesome-templates/login-template";

function AdminPage() {
    return (
        <div className="text-white">
            <HomeTemplate>
                <section class="white text-dark section-transition section-fullwindow">
                    //write code here
                </section>
            </HomeTemplate>
            <HomeFooter />
        </div>
    );
}

export default AdminPage;