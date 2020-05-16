import React from 'react';
import './App.css';
import 'antd/dist/antd.css';
import CustomLayout from './components/containers/Layout';
import Heading from './components/static/Heading';

function App() {
  return (
    <div className="App">
        <CustomLayout>
          <Heading/>
        </CustomLayout>
    </div>
  );
}

export default App;
