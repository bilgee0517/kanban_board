import React, { useState } from 'react';
import { Container, Button } from 'react-bootstrap';
import AddTask from './pages/AddTask';
import KanbanBoard from './pages/KanbanBoard';

export default function App() {
  const [showAddTaskModal, setShowAddTaskModal] = useState(false);

  const handleClose = () => setShowAddTaskModal(false);
  const handleShow = () => setShowAddTaskModal(true);

  return (
    <Container>
      <KanbanBoard />
      <Container>
        <Button variant="primary" onClick={handleShow}>
          Add Task
        </Button>
        <AddTask show={showAddTaskModal} handleClose={handleClose} />
      </Container>
     </Container>
  );
}

