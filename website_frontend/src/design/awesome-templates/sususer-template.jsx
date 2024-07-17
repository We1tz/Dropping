import { useEffect, useState } from 'react';
import { BarChart, Bar, Rectangle, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line, PieChart, Pie, Sector   } from 'recharts';
import AnalitService from '../../API/AnalitService';
import { color } from 'd3';
/*
const data = [
    {
      name: 'Page A',
      uv: 4000,
      pv: 2400,
      amt: 2400,
    },
    {
      name: 'Page B',
      uv: 3000,
      pv: 1398,
      amt: 2210,
    },
    {
      name: 'Page C',
      uv: 2000,
      pv: 9800,
      amt: 2290,
    },
    {
      name: 'Page D',
      uv: 2780,
      pv: 3908,
      amt: 2000,
    },
    {
      name: 'Page E',
      uv: 1890,
      pv: 4800,
      amt: 2181,
    },
    {
      name: 'Page F',
      uv: 2390,
      pv: 3800,
      amt: 2500,
    },
    {
      name: 'Page G',
      uv: 3490,
      pv: 4300,
      amt: 2100,
    },
  ];
*/
  const renderActiveShape = (props) => {
    const RADIAN = Math.PI / 180;
    const { cx, cy, midAngle, innerRadius, outerRadius, startAngle, endAngle, fill, payload, percent, value } = props;
    const sin = Math.sin(-RADIAN * midAngle);
    const cos = Math.cos(-RADIAN * midAngle);
    const sx = cx + (outerRadius + 10) * cos;
    const sy = cy + (outerRadius + 10) * sin;
    const mx = cx + (outerRadius + 30) * cos;
    const my = cy + (outerRadius + 30) * sin;
    const ex = mx + (cos >= 0 ? 1 : -1) * 22;
    const ey = my;
    const textAnchor = cos >= 0 ? 'start' : 'end';

      
  
  
    return (
      <g>
        <text x={cx} y={cy} dy={8} textAnchor="middle" fill={fill}>
          {payload.name}
        </text>
        <Sector
          cx={cx}
          cy={cy}
          innerRadius={innerRadius}
          outerRadius={outerRadius}
          startAngle={startAngle}
          endAngle={endAngle}
          fill={fill}
        />
        <Sector
          cx={cx}
          cy={cy}
          startAngle={startAngle}
          endAngle={endAngle}
          innerRadius={outerRadius + 6}
          outerRadius={outerRadius + 10}
          fill={fill}
        />
        <path d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`} stroke={fill} fill="none" />
        <circle cx={ex} cy={ey} r={2} fill={fill} stroke="none" />
        <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} textAnchor={textAnchor} fill="#333">{`PV ${value}`}</text>
        <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} dy={18} textAnchor={textAnchor} fill="#999">
          {`(Rate ${(percent * 100).toFixed(2)}%)`}
        </text>
      </g>
    );
  };

export default function SusUserTemplate(props) {
    const [amm, setAmm] = useState(10);
    const [data, setData] = useState([]);
    const [srdang, setSrdang] = useState();

    const [diagdata, setDiagdagta] = useState([]);
    useEffect(() => {
        const a = AnalitService.getaboutprofile(props.id).then(function(res){
            setData(res.data.transfers);
            setSrdang(res.data.midlle_danger);
            console.log(res.data);

            for(let i = 0; i < res.data.transfers.length; i++){
              setDiagdagta([...diagdata, res.data.transfers[i].ammount]);
            }
          });
    }, []);
    const showmore = ()=>{
        setAmm(amm+10);
    };

  const [state, setState] = useState({
    activeIndex: 0,
  });

  const onPieEnter = (_, index) => {
    setState({
      activeIndex: index,
    });
  };
  
  const data_pie = [
    { name: '% опасности', value: srdang, fill:"red" },
    { name: '% безопасности', value: 1-srdang },
  ];

  return (
    <>
    <div >
        <div className="row">
            <div className='col'>
            <div class="bg-dark">
            <BarChart
              width={500}
              height={300}
              data={diagdata.slice(0, amm)}
              margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="pv" fill="#5a64ed" activeBar={<Rectangle fill="#cf4cd4" stroke="black" />} />
              <Bar dataKey="uv" fill="#ed5f42" activeBar={<Rectangle fill="#d4a04c" stroke="black" />} />
            </BarChart>
            <PieChart width={400} height={400}>
          <Pie
            activeIndex={state.activeIndex}
            activeShape={renderActiveShape}
            data={data_pie}
            cx="50%"
            cy="50%"
            innerRadius={60}
            outerRadius={80}
            fill="#8884d8"
            dataKey="value"
            onMouseEnter={onPieEnter}
          />
        </PieChart>
            </div>
            </div>
            <div className='col span-3'>
            <table class="table table-dark">
    <thead>
        <tr>
        <th scope="col">Сумма</th>
        <th scope="col">Коэфф. опасности</th>
        <th scope="col">Время перевода</th>
        <th scope="col">Получатель</th>
    </tr>
  </thead>
  <tbody>
    {
      data.length > 0 ? 
      data.map((i, index)=>{
      return(      
      <tr key={index}>
        <td >{i.ammount}</td>
        <td>{i.danger*100}% </td>
        <td>{i.date}</td>
        <td><a href = {'/SusUserPage/' + i.out_account.toString()} /*Не пишите комментарии, эта жопа может принять их за код :D p.s. ГОООООЛ*/ >{i.out_account.substring(0, 10)}...</a></td>

      </tr>)
    }): <h1 className='text-white'>Загрузка...</h1>}
  </tbody>
</table>

{/*
  amm < data.length ? 
  <><button type="button" className="btn btn-primary" onClick={() => {showmore()}}>Показать еще</button></>
  :
  "" 
*/}
            </div>
        </div>
    </div>
        
    </>
  )
}
