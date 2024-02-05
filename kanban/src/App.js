import React from 'react';
import Tasks from './components/Tasks';
import Header from './components/Header'; 
import Container from 'react-bootstrap/Container';

function App() {
  return (
    <Container fluid className="App">
      <Header />
      <Tasks />
    </Container>
  );
}

export default App;