import React, { useEffect, useState } from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';
import { observer } from 'mobx-react-lite';
import VictorineService from '../../API/VictorineService';
import { useContext } from 'react';
import {Context} from "../../main";
import { useParams } from 'react-router-dom';

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function VictorineTemplate() {
    const {id} = useParams();

    const {store} = useContext(Context);

    const [picnum, setPicNum] = useState(getRandomInt(1, 6)); 
    const [rightans, setRightans] = useState(0);
    const [over, setOver] = useState(false);

    const [date, setDate] = useState(Date.now());
    
    const [cnt, setcnt] = useState(1);
    
    const answers = {
        1: true,
        2: true,
        3: true,
        4: true,
        5: true,
        6: true,
        7: false,
        8: false,
        9: true,
        10: true,
        11: true,
        12: true,
        13: false,
        14: false,
        15: false,
        16: false,
        17: false,
        18: false,
        19: false,
        20: true,
        21: true,
        22: false,
    }

    async function HandleClick(yes){
        if(cnt==10){
            //
            setOver(true);
            setDate(Date.now()-date);
            console.log(store.user.username);
            if(id != undefined){
                await VictorineService.Sendres(id, rightans, date);
            }else{
                await VictorineService.Sendres(NaN, rightans, date);
            }
        }
        if(yes == answers[picnum]){
            setRightans(rightans+1);
        }
        setcnt(cnt+1);
        setPicNum(picnum+1);
    }

    return (
        <div class="text-dark">
            <section class="section-transition section-fullwindow">
                <div class="container">
                    <div class="row">
                    <div class="col-sm">
                        {over ? <>
                            <h2 className='text-light'>Время: {date.toString().substring(0, date.toString().length-3)} секунд, Правильных ответов: {rightans} из 10</h2>
                            <br />
                            <br />
                            <br />
                        </>:
                            <>
                            <h1 className='text-start text-light fw-bold'>Вакансия {cnt}</h1>
                        <h3 className='text-start text-light fw-bold'>Является ли вакансия дроппинговой?</h3>
                            <div className='jumbotron'>
                                <div class="row">
                                    <div class="col-4">
                                        <input type="submit" onClick={()=>HandleClick(true)} value="ДА" class="btn btn-lg btn-square btn-warning float-left"/>
                                    </div>
                                    <div class="col-4 d-flex justify-content-center">
                                    </div>
                                    <div class="col-4">
                                    <input type="submit" onClick={()=>HandleClick(false)} value="НЕТ" class="btn btn-lg btn-square btn-warning float-right"/>
                                </div>
                            </div>
                            </div>
                            <br />
                            <br />
                            <br />
                            <p></p>
                            </>
                        }
                        </div>
                        <div class="col-sm">
                            {over ? 
                                <img className='victorine-pic' src="fox.png" alt="" />
                            : <>

                                {picnum <=6 ?
                                <img className='victorine-pic' height={"100px"} src={"Вакансии викторины/Вакансия"+ picnum + ".png"} alt="" />
                            :
                                <img className='victorine-pic' src={"Вакансии викторины/Вакансия"+ picnum + ".jpg"} alt="" />
                            }
                            </>
                            }
                        </div>
                        
                    </div>
                </div>
            </section>

        </div>
    );
}

export default observer(VictorineTemplate);