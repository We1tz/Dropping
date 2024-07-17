import HomeFooter from "../awesome-components/footers/footer-home";
import CurveTransitionTemplate from "../awesome-templates/curve-transition-template";
import HomeTemplate from "../awesome-templates/home-template";

function HomePage() {
    return ( 
        <>
            <HomeTemplate>
                <CurveTransitionTemplate />
            </HomeTemplate>
            <HomeFooter />
        </> 
    );
}

export default HomePage;