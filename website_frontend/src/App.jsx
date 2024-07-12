import React, {useEffect, useContext} from 'react';
import Home from './design/awesome-templates/home-template.jsx';
import HomeFooter from './design/awesome-components/footers/footer-home.jsx';
import MiniFooter from './design/awesome-components/footers/footer-mini.jsx';
import CurveTransitionTemplate from './design/awesome-templates/curve-transition-template.jsx';
import { Context } from './main.jsx';
import { createRoot } from "react-dom/client";
import { BrowserRouter, Route, Routes} from "react-router-dom";
import {observer} from "mobx-react-lite";
import "./curves.scss";
import HomePage from './design/pages/home-page.jsx';
import LoginFormPage from './design/pages/login-page.jsx';
import ProfilePage from './design/pages/profile-page.jsx';
import AdminPage from './design/pages/admin-page.jsx';
import RatingPage from './design/pages/rating-page.jsx';
import RegisterFormPage from './design/pages/register-page.jsx';
import VictorinePage from './design/pages/victorine-page.jsx';
import RestorePage from './design/pages/restore-page.jsx';
import GraphPage from './design/pages/graphs-page.jsx';
import NewpassPage from './design/pages/newpass-page.jsx';
import NFPage from './design/pages/nf-page.jsx';

function App() {
  const {store }= useContext(Context);
  useEffect(() => {
    if (localStorage.getItem('token')) {
        store.checkAuth()
    }
}, [])

if (store.isLoading) {
  return <div>Загрузка...</div>
}
  return (
    <div align="center">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.0/css/all.css" />
      <script defer src="https://use.fontawesome.com/releases/v5.1.0/js/all.js"></script>

      <BrowserRouter basename="/">
        <Routes>
          <Route path="/" element={<HomePage/>} />
          <Route path="/rating" element={<RatingPage/>} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/login" element={<LoginFormPage />} />
          <Route path="/restorepass" element={<RestorePage />} />
          <Route path="/admin" element={<AdminPage />} />
          <Route path="/register" element={<RegisterFormPage/>} />
          <Route path="/victorine" element={<VictorinePage/>} />
          <Route path="/graph" element={<GraphPage/>} />
          <Route path="/newpass" elemant={<NewpassPage/>} />
          <Route path='*' element={<NFPage/>}/>
        </Routes>
      </BrowserRouter>

    </div>
  );
}


export default observer(App);
