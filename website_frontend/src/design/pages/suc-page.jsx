import React from 'react'
import HomeTemplate from '../awesome-templates/home-template'
import HomeFooter from '../awesome-components/footers/footer-home'

export default function SucPage() {
  return (
    <>
      <HomeTemplate>
        
      <section class=" section-article section-fullwindow">
                <h1 className='display-4 text-light'>Добро пожаловать</h1>
                <h1 className='display-4 text-light'>Вы успешно подтвердили почту</h1>
            </section>
        </HomeTemplate>
      <HomeFooter />
    </>
  )
}