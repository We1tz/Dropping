import { useCallback } from 'react';
import ReactFlow, { addEdge, useEdgesState, useNodesState, ReactFlowProvider, MiniMap } from 'reactflow';
import 'reactflow/dist/style.css';
import Aboba from './aboba.jsx';
import initialNodes from './testdata/nodes.js';
import initialEdges from './testdata/edges.js';

function Flow() {
  

  return (
    <div >
        <div className='constainer'>
            <div className='row'>
            <div class="col">
                
            </div>
            <div class="col"style={{height:700, width:500}} >
            <Aboba/>
            </div>
            </div>
        </div>
        
    </div>
  );
}

function GraphTemplate(props) {
    return (
      <ReactFlowProvider>
        <Flow/>
      </ReactFlowProvider>
    );
  }

export default GraphTemplate;