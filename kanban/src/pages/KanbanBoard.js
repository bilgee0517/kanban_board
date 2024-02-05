import React from 'react';
import { Container, Stack } from 'react-bootstrap';
import Tasks from '../components/Tasks'; 
import Header from '../components/Header';

export default function KanbanBoard() {
    return (
    <Container fluid className='KanbanBoard' style={{ height: '100vh' }}>
         <Header />
        <Stack direction='horizontal' gap={3} style={{ display: 'flex' }}>
            <Container className="kanban-column" style={{ flex: 1 }}>
                <h3>Todo</h3>
                <Tasks status="todo" />
            </Container>
            <Container className="kanban-column" style={{ flex: 1 }}>
                <h3>In Progress</h3>
                <Tasks status="in-progress" />
            </Container>
            <Container className="kanban-column" style={{ flex: 1 }}>
                <h3>Done</h3>
                <Tasks status="done" />
            </Container>
        </Stack>
    </Container>
  );
}

