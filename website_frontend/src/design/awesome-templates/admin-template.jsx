import React, { useEffect, useState } from 'react'
import { observer } from 'mobx-react-lite';
import DroppersList from './droppers-list';
import Aboba from './aboba';
import AnalitService from '../../API/AnalitService';
import { useNavigate } from 'react-router-dom';

function AdminTemplate() {
  const navigate = useNavigate();
  
  const [data2, setData2] = useState([]);

  async function fetchData() {
    const a = await AnalitService.AgressiveUsers().then(r => {console.log(r.data.information); setData2(r.data.information)});
    return a
  }
  useEffect(()=>{
    fetchData();
  }, []);

  const handleclick = (id) => {
    navigate(`/SusUserPage/${id}`);
  }

  return (
    <div className='constainer grad-article'>
      <section className='section-article section-fullwindow'>
      <table class="table table-dark">
    <thead>
        <tr>
        <th scope="col">Вердикт</th>
        <th scope="col">ID пользователя</th>
        <th scope="col">Сумма перевода</th>
        <th scope="col">Время перевода</th>
        <th scope="col">id отправителя</th>
        <th scope="col">id получателя</th>
    </tr>
  </thead>
  <tbody>
    {
      data2.length > 0 ? 
    data2.map((i, index)=>{
      return(      
      <tr key={index}>
        <th scope="row">{index+1}</th>
        <td >{i.id}</td>
        <td>{i.ammount} руб</td>
        <td>{i.date}</td>
        <td><a href = {'/SusUserPage/' + i.account_id.toString()} /*Не пишите комментарии, эта жопа может принять их за код :D p.s. ГОООООЛ*/ >{i.account_id.substring(0, 10)}...</a></td>
        <td><a href = {'/SusUserPage/' + i.account_out.toString()} /*Не пишите комментарии, эта жопа может принять их за код :D p.s. ГОООООЛ*/ >{i.account_out.substring(0, 10)}...</a></td>
      </tr>)
    }): <h1 className='text-white'>Загрузка...</h1>}
  </tbody>
</table>
      </section>
            
        </div>
  )
}

export default observer(AdminTemplate);