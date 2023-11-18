import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const response = await fetch('/api/data');
    const jsonData = await response.json();
    setData(jsonData);
  };

  return (
    <div>
      <h1>Node.js and React.js Template</h1>
      {data && <p>{data.message}</p>}
    </div>
  );
}

export default App;