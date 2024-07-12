import React from 'react'
import HomeTemplate from '../awesome-templates/home-template'
import HomeFooter from '../awesome-components/footers/footer-home'

export default function NFPage() {
  return (
    <>
      <HomeTemplate>
        
      <section class=" section-article section-fullwindow">
                <h1 className='display-4 text-light'>404</h1>
                <h1 className='display-4 text-light'>Page Not Found</h1>
            </section>
        </HomeTemplate>
      <HomeFooter />
    </>
  )
}
