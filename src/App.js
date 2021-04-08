import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [currentTime, setCurrentTime] = useState(0);
  
  const [currentTest, setTest] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  useEffect(() => {
    fetch('/test').then(res => res.json()).then(data => {
      console.log('do i execute')
      setTest(data.testvar);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...
      
        <p>The current time is  {currentTime}.</p>
        <p>The variable from Flask is {currentTest}.</p>
        

      </header>
    </div>
  );
}

export default App;