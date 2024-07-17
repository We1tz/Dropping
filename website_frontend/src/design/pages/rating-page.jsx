import HomeFooter from "../awesome-components/footers/footer-home";
import CurveTransitionTemplate from "../awesome-templates/curve-transition-template";
import HomeTemplate from "../awesome-templates/home-template";
import RatingTemplate from "../awesome-templates/rating-template";

function RatingPage() {
    return ( 
        <>
            <HomeTemplate>
                <RatingTemplate />
            </HomeTemplate>
            <HomeFooter />
        </> 
    );
}

export default RatingPage;