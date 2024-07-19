import React, {useEffect, useState} from 'react';
import CurveTransition from '../awesome-components/transitions/curve-transition';
import BubbleTransition from '../awesome-components/transitions/bubble-transition';
import WaveTransition from '../awesome-components/transitions/wave-transition';
import { observer } from "mobx-react-lite";
function CurveTransitionTemplate() {

    useEffect(() =>{
        fetch("../../../../public/index.json")
                    .then(res => res.json())
                    .then(res => res.files)
                    .catch(err => console.log(err));
    });
    return (
        <div class="text-light grad-article">
            Please Stand By...
        </div>
    );
}

export default observer(CurveTransitionTemplate);