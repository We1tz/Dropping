import React, { useEffect, useState } from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function VictorineTemplate() {

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

    function HandleClick(yes){
        if(cnt==10){
            setOver(true);
            setDate(Date.now()-date);
        }
        if(yes == answers[picnum]){
            setRightans(rightans+1);
        }
        setcnt(cnt+1);
        setPicNum(picnum+1);
    }

    return (
        <div class="text-dark">
            <section class="light section-transition section-fullwindow">
                <div class="container">
                    <div class="row">
                        <div class="col-sm">
                            {over ? "": <>

                                {picnum <=6 ?
                                <img className='victorine-pic' src={"Вакансии викторины/Вакансия"+ picnum + ".png"} alt="" />
                            :
                                <img className='victorine-pic' src={"Вакансии викторины/Вакансия"+ picnum + ".jpg"} alt="" />
                            }
                            </>}
                        </div>
                        <div class="col-sm">
                        {over ? <>
                            <h2>Время: {date}, Правильных ответов: {rightans}</h2>
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
                                <h2>{date}</h2>
                            </div>
                            </div>
                            </>
                        }
                        </div>
                    </div>
                </div>
            </section>

        </div>
    );
}

export default VictorineTemplate;