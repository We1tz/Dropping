import React, { useEffect, useState } from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';
import { observer } from 'mobx-react-lite';
import axios from 'axios';
import VictorineService from '../../API/VictorineService';

let amm = 10;
function RatingTemplate() {

  const [data, setData] = useState(Getres(0, amm));
  async function showmore(){
    setData([...data, await VictorineService.Getres(amm, amm+10)]);
    amm = amm + 10;
  };
    return (
        <div class="text-dark grad-article">
            
            <section class=" section-article section-fullwindow">
                <h1 className='display-4 text-sm-start'>Рейтинг</h1>
                    <div class="container">
                    <table class="table">
  <thead>
    <tr>
      <th scope="col">Место</th>
      <th scope="col">Имя пользователя</th>
      <th scope="col">Баллы</th>
      <th scope="col">Время прохождения</th>
    </tr>
  </thead>
  <tbody>
    {
    SlicedData.map((i, index)=>{
      return(      
      <tr key={index}>
        <th scope="row">{index+1}</th>
        <td >{i.name}</td>
        <td>{i.score}</td>
        <td>{i.time}</td>
      </tr>)
    })}
  </tbody>
</table>
{
  amm < data.length ? 
    <><button type="button" className="btn btn-primary" onClick={() => {showmore()}}>Показать еще</button></>
   : ""
}

                    </div>
                
            </section>

        </div>
    );
}

export default observer(RatingTemplate);