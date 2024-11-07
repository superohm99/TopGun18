import logo from './logo.svg';
import './App.css';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, Label} from 'recharts'
import React, { useEffect, useState} from 'react';
import io from 'socket.io-client'

const socket = io('http://localhost:5888', {
  autoConnect:true
})

function Socket() {
  const [message, setMessage] = useState([]);

  useEffect(() => {
    socket.connect();

    return () => {
      socket.disconnect();
    };
  }, []);

  useEffect(() => {
    socket.on('response', (response) => {
      console.log('Server response back:', response);
      setMessage([...message, response]);
    })
    return () => {
      socket.off("response");
    };
  }, [message])

  function sendMessage(){
    socket.emit('message',"Hello server");
  }
  const messageList = message.map((_message,_index)=><li>{_index} {_message}</li>)
  return (<div className='App'> <ul>{messageList}</ul><button onClick={sendMessage}>Great</button></div>);
}


function generateRandomData() {
  const startDate = new Date('2024-02-14T00:00:00Z');
  const endDate = new Date('2024-02-15T00:00:00Z');
  const intervalMinutes = 15;

  const data = [];
  let currentTime = startDate;

  while (currentTime <= endDate) {
    const timestamp = currentTime.toISOString();
    const x = Math.random()

    data.push({ timestamp, x });

    currentTime = new Date(currentTime.getTime() + intervalMinutes * 60 * 1000);
  }

  return data;
}

function App() {

  const data = generateRandomData();
  return (
    <div className="App">
        <LineChart width={1000} height={300} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="timestamp" />
        <YAxis yAxisId="left">
          <Label value="mm/s" position="insideLeft" angle={-90}/>
        </YAxis>
        <Tooltip/>
        <Legend/>
        <Line type="monotone" dataKey="x" stroke='#8884d8' yAxisId="left" dot={false} />
        </LineChart>

        <Socket />
    </div>
  );
}

export default App;
