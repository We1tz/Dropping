import HomeFooter from "../awesome-components/footers/footer-home";
import CurveTransitionTemplate from "../awesome-templates/curve-transition-template";
import HomeTemplate from "../awesome-templates/home-template";
import VictorineTemplate from "../awesome-templates/victorine-template";

function VictorinePage() {
    return ( 
        <>
            <HomeTemplate>
                <VictorineTemplate />
            </HomeTemplate>
            <HomeFooter />
        </> 
    );
}

export default VictorinePage;