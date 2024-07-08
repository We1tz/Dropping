import React, { useEffect, useState } from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';
import { observer } from 'mobx-react-lite';

function RatingTemplate() {
  const [data, setData] = useState([
    {name:"jopa", time:"1245"},
    {name:"jopa", time:"1245"},
    {name:"jopa", time:"1245"},
  ]);

  useEffect(()=>{
    console.log(data[0].time);
  }, []);
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
    data.map((i, index)=>{
      return(      
      <tr>
        <th scope="row">{index+1}</th>
        <td>{i.name}</td>
        <td>Last</td>
        <td>{i.time}</td>
      </tr>)
    })}
  </tbody>
</table>
                    </div>
                
            </section>

        </div>
    );
}

export default observer(RatingTemplate);