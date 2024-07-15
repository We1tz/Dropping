import HomeFooter from "../awesome-components/footers/footer-home";
import CurveTransitionTemplate from "../awesome-templates/curve-transition-template";
import HomeTemplate from "../awesome-templates/home-template";
import SusUserTemplate from "../awesome-templates/sususer-template";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import React from "react";
import { useState } from "react";
import AnalitService from "../../API/AnalitService";

function SusUserPage() {
    const { id } = useParams();
   
    return ( 
        <>
            <HomeTemplate>
            <div class="text-dark">
                    <SusUserTemplate id = {id}/>
                </div>
            </HomeTemplate>
            <HomeFooter />
        </> 
    );
}

export default SusUserPage;