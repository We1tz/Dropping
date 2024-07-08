import React, { useEffect } from 'react';
import { useContext } from 'react';
import {Context} from "../../main";
import { observer } from "mobx-react-lite";

function Navbar() {
    useEffect(() =>{
        console.log(store.isAuth);
    }, []);
    const {store} = useContext(Context);
    return (
        <div>
            <nav className="navbar navbar-colapse navbar-expand-lg bg-dark" data-bs-theme="dark" expand="lg">
                <div className="container-fluid">
                    <a class="navbar-brand" href="#">Foxproof</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">

                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto">
                            <li className="nav-item">
                                <a data-testid="home-link" className="nav-link active" href="/">Главная</a>
                            </li>
                            <li>
                            <a data-testid="home-link" className="nav-link active" href="/rating">Рейтинг</a>
                            </li>
                            {
                                store.isAuth?
                                <>
                                <li>
                        <a data-testid="home-link" className="nav-link active" href="/victorine">Викторина</a>
                        </li>
                        <li>
                        <a data-testid="home-link" className="nav-link active" href="/graph">Аналитика</a>
                        </li>
                                </>
                                    :
                                    ""
                            }
                            
                        </ul>
                        {store.isAuth?
                                        <a data-testid="home-link" className="nav-link text-light" onClick={() => store.logout()}>Выйти</a>
                                    :
                                        <a data-testid="home-link" className="nav-link text-light" href="/register">Регистрация</a>
                        }
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default observer(Navbar);