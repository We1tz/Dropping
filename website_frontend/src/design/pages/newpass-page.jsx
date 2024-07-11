import React from "react";
import HomeTemplate from "../awesome-templates/home-template";
import NewpassTemplate from '../awesome-templates/newpass-template';

function NewpassPage(){
    return (
        <div>
            <HomeTemplate>
                <section class="section-transition grad-article section-fullwindow">
                    <div className="login-jumbotron text-light">
                        <img height="150" width="150" src="fox-logo.png" alt="" />
                        <h1 className="bold">Foxproof</h1>
                        
                        <NewpassTemplate />
                    </div>
                </section>
            </HomeTemplate>
        </div>
    )
}
export default NewpassPage;