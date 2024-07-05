import React, { useEffect } from 'react'
import GraphTemplate from '../awesome-templates/graph-template';
import HomeTemplate from '../awesome-templates/home-template';
import HomeFooter from '../awesome-components/footers/footer-home';


function GraphPage() {
  return (
    <div>
      <HomeTemplate>
        <GraphTemplate/>
      </HomeTemplate>
      <HomeFooter />
    </div>
  )
}

export default GraphPage;