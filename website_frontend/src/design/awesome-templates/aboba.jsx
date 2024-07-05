import { useCallback } from 'react';
import ReactFlow, { addEdge, useEdgesState, useNodesState, ReactFlowProvider, MiniMap } from 'reactflow';
import 'reactflow/dist/style.css';

import initialNodes from './testdata/nodes.js';
import initialEdges from './testdata/edges.js';

export default function Aboba() {
    const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges]
  );

  return (
    <div style={{ height: 800 }}>
        <ReactFlow defaultNodes={nodes} defaultEdges={edges} fitView>
            <MiniMap nodeColor="#32a852" nodeStrokeWidth={3} zoomable pannable />
        </ReactFlow>
    </div>
  )
}
