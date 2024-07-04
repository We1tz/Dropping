import React from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';


function RatingTemplate() {
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
      <th scope="col">Last</th>
      <th scope="col">Время прохождения</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Larry</td>
      <td>the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
                    </div>
                
            </section>

        </div>
    );
}

export default RatingTemplate;