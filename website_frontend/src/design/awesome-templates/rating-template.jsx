import React, { useEffect, useState } from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';
import { observer } from 'mobx-react-lite';
import axios from 'axios';
import VictorineService from '../../API/VictorineService';

function RatingTemplate() {
  const [amm, setAmm] = useState(10);
  const [data, setData] = useState([]);
  useEffect(()=>{
    const a = VictorineService.Getres().then(function(res){
      setData(res.data);
      console.log(res.data);
    });
  }, []);

  const showmore = ()=>{
    setAmm(amm+10);
  }
    return (
        <div class="text-dark grad-article">
            
            <section class=" section-article section-fullwindow">
                <h1 className='display-4 text-sm-start text-light'>Рейтинг</h1>
                    <div class="container">
                    <table class="table table-dark">
  <thead>
    <tr>
      <th scope="col">Место</th>
      <th scope="col">Имя пользователя</th>
      <th scope="col">Баллы</th>
    </tr>
  </thead>
  <tbody>
    {
    data.slice(0, amm).map((i, index)=>{
      return(      
      <tr key={index}>
        <th scope="row">{index+1}</th>
        <td >{i.username}</td>
        <td>{i.score}</td>
      </tr>)
    }) }
  </tbody>
</table>
{
  amm < data.length ? 
    <><button type="button" className="btn btn-info" onClick={() => {showmore()}}>Показать еще</button></>
   : ""
}

                    </div>
                
            </section>

        </div>
    );
}

export default observer(RatingTemplate);