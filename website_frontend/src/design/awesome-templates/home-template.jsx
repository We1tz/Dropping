import React from 'react';
import Navbar from '../awesome-components/navbar-default.jsx';
import { observer } from "mobx-react-lite";
function HomeTemplate(props) {
    return ( 
        <div>
            <div className="text-dark ">
                <Navbar />
                {props.children}
            </div>
        </div>
    );
}

export default observer(HomeTemplate);