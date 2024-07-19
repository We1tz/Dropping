import React, {useEffect, useState} from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';
import { observer } from "mobx-react-lite";

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
            <div className="list">
                <div className="row">
                    {posts.map((post) => (
                        <div class="card bg-dark text-white" >
                        <img  class="card-img-top" src={post.img}/>
                        <div class="card-body">
                          <h5 class="card-title">{post.title}</h5>
                          <p class="card-text">{post.annotation}</p>
                          <a href={"/post/"+post.id} class="btn btn-info">Читать</a>
                        </div>
                      </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default observer(CurveTransitionTemplate);