import React, { useEffect, useState } from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';


function VictorineTemplate() {

    const [picnum, setPicNum] = useState(1); 
    const [rightans, setRightans] = useState(0);
    const [over, setOver] = useState(false);

    const [date, setDate] = useState(Date.now());

    function HandleClick(yes){
        if(picnum==10){
            setOver(true);
            setDate(Date.now()-date);
        }
        if(yes){
            setRightans(rightans+1);
        }
        setPicNum(picnum+1);
    }

    return (
        <div class="text-dark">
            <section class="light section-transition section-fullwindow">
                <div class="container">
                    <div class="row">
                        <div class="col-sm">
                            <img src="fox.png" alt="" />
                        </div>
                        <div class="col-sm">
                        {over ? <h2>{date}</h2>:
                            <>
                            <h1 className='text-start text-light fw-bold'>Вакансия {picnum}</h1>
                        <h3 className='text-start text-light fw-bold'>Является ли вакансия дроппинговой?</h3>
                            <div className='jumbotron'>
                                <div class="row">
                                    <div class="col-4">
                                        <input type="submit" onClick={()=>HandleClick(false)} value="ДА" class="btn btn-lg btn-square btn-warning float-left"/>
                                    </div>
                                    <div class="col-4 d-flex justify-content-center">
                                    </div>
                                    <div class="col-4">
                                    <input type="submit" value="НЕТ" class="btn btn-lg btn-square btn-warning float-right"/>
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