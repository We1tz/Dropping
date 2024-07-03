import HomeFooter from "../awesome-components/footers/footer-home";
import BubbleTransition from "../awesome-components/transitions/bubble-transition";
import CurveTransition from "../awesome-components/transitions/curve-transition";
import HomeTemplate from "../awesome-templates/home-template";
import LoginForm from "../awesome-templates/login-template";
import { useState } from "react";

function ProfilePage() {
    return (
        <div className="text-white">
            <HomeTemplate>
            </HomeTemplate>
            <HomeFooter />
            
        </div>
    );
}

export default ProfilePage;