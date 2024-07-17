import React from 'react'
import HomeTemplate from "../awesome-templates/home-template";
import RestoreTemplate from '../awesome-templates/restore-template';

export default function RestorePage() {
  return (
    <div className="text-white ">
            <HomeTemplate>
                <section class="section-transition grad-article section-fullwindow">
                    <div className="login-jumbotron text-light">
                        <img height="150" width="150" src="fox-logo.png" alt="" />
                        <h1 className="bold">Foxproof</h1>
                        
                        <RestoreTemplate />
                    </div>
                </section>
            </HomeTemplate>
        </div>
  )
}
