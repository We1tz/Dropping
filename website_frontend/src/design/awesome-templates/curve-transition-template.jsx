import React, {useEffect, useState} from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';
import { observer } from "mobx-react-lite";
import Carousel from "react-multi-carousel";

const responsive = {
    superLargeDesktop: {
      // the naming can be any, depends on you.
      breakpoint: { max: 4000, min: 3000 },
      items: 5
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 3
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1
    }
  };

function CurveTransitionTemplate() {

    const [posts, setPosts] = useState([]);

    useEffect(() =>{
        fetch("/index.json")
                    .then(res => res.json().then((result) =>{
                        setPosts(result.files);
                    }));
    });
    return (
        <div class="text-light grad-article">
            <div className="padding-bottom">
                    {posts.map((post) => (
                        <div class="card bg-dark text-white container d-flex flex-column" >
                            <img  class="card-img-top" src={post.img}/>
                            <div class="card-body  flex-">
                                <h5 class="card-title">{post.title}</h5>
                                <p class="card-text">{post.annotation}</p>
                                    <a href={"/post/"+post.id} class="btn btn-info mt-auto" style={{marginTop:"10px"}}>Читать</a>
                            </div>
                        </div>
                    ))}
            </div>
            <br /><br /><br />
        </div>
    );
}


/*
<div class="card bg-dark text-white container d-flex flex-column" >
                            <img  class="card-img-top" src={post.img}/>
                            <div class="card-body">
                                <h5 class="card-title">{post.title}</h5>
                                <p class="card-text">{post.annotation}</p>
                                <div className='card-footer'>
                                    <a href={"/post/"+post.id} class="btn btn-info " style={{marginTop:"10px"}}>Читать</a>
                                </div>
                            </div>
                        </div>
*/

export default observer(CurveTransitionTemplate);