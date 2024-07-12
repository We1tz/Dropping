import HomeFooter from "../awesome-components/footers/footer-home";
import BubbleTransition from "../awesome-components/transitions/bubble-transition";
import CurveTransition from "../awesome-components/transitions/curve-transition";
import HomeTemplate from "../awesome-templates/home-template";
import LoginForm from "../awesome-templates/login-template";
import AdminTemplate from "../awesome-templates/admin-template";

function AdminPage() {
    return (
        <div className="text-white">
            <HomeTemplate>
                <AdminTemplate/>
            </HomeTemplate>
            <HomeFooter />
        </div>
    );
}

export default AdminPage;