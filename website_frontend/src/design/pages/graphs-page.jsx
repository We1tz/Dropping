import React, { useEffect } from 'react'
import Flow from '../awesome-templates/analitycs-template';
import HomeTemplate from '../awesome-templates/home-template';
import HomeFooter from '../awesome-components/footers/footer-home';


function GraphPage() {
  return (
    <div>
      <HomeTemplate>
        <Flow/>
      </HomeTemplate>
      <HomeFooter />
    </div>
  )
}

export default GraphPage;