import HomeFooter from "../awesome-components/footers/footer-home";
import CurveTransitionTemplate from "../awesome-templates/curve-transition-template";
import HomeTemplate from "../awesome-templates/home-template";
import SusUserTemplate from "../awesome-templates/sususer-template";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import React from "react";
import { useState } from "react";
function SusUserPage() {
    const { id } = useParams();
    useEffect(() => {
        console.log(id);
    }, [])
    return ( 
        <>
            <HomeTemplate>
                <SusUserTemplate/>
            </HomeTemplate>
            <HomeFooter />
        </> 
    );
}

export default SusUserPage;