const express = require('express');
const app = express();

// API routes
app.get('/api/data', (req, res) => {
  // Handle API request and return data
  const data = { message: 'Hello, World!' };
  res.json(data);
});

// Serve static files
app.use(express.static('client/build'));

// Handle production environment
if (process.env.NODE_ENV === 'production') {
  // Serve static files from React app
  app.use(express.static('client/build'));

  // Return index.html for all remaining routes
  app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'client', 'build', 'index.html'));
  });
}

// Start server
const port = process.env.PORT || 5000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});