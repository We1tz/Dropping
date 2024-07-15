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
    const [data, setData] = useState([]);
    const fetchData = async () => {
        const a = await AnalitService.AgressiveUsers().then(r => {console.log(r.data.information); setData(r.data.information)});
        return a
    }; // запросить данные с сервера по id пользователя
    useEffect(() => {
        console.log(id);
        fetchData();
    }, []);
    return ( 
        <>
            <HomeTemplate>
                {data.length > 0 ?
                    <SusUserTemplate req = {data}/>
                :
                    <h1 className="">Загрузка...</h1>
                }
                
            </HomeTemplate>
            <HomeFooter />
        </> 
    );
}

export default SusUserPage;