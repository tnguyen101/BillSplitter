const express = require('express');
const path = require('path');
const app = express();

// Serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/manage', (req, res) => {
    res.sendFile(path.join(__dirname, 'manage.html'));
});

app.get('/people', (req, res) => {
  res.sendFile(path.join(__dirname, 'people.html'));
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});