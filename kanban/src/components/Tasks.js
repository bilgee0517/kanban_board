import React, { useState, useEffect } from 'react';

export default function Tasks({ status }) {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const response = await fetch('/tasks');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setTasks(data.tasks);
      } catch (error) {
        console.log('Error fetching tasks:', error);
      }
    };

    fetchTasks();
  }, []);

  // Filter tasks based on the status prop
  const filteredTasks = tasks.filter(task => task.status === status);

  return (
    <div>
      {filteredTasks.map(task => (
        <div key={task.id}>
          <h2>{task.title}</h2>
          <p>{task.description}</p>
        </div>
      ))}
    </div>
  );
}
