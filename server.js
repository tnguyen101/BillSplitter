const express = require('express');
const path = require('path');
const { spawn } = require('child_process');  // Importing spawn
const app = express();

// Middleware to parse JSON and URL-encoded bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

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

app.get('/data.json', (req, res) => {
  res.sendFile(path.join(__dirname, 'data.json'));
});

app.get('/receipt_data2.json', (req, res) => {
  res.sendFile(path.join(__dirname, 'receipt_data2.json'));
});


//endpoints to functions

// Endpoint to call the Python script
app.post('/add_receipt', (req, res) => {
  const name = req.body.name;
  const price = req.body.price;
  const people = req.body.people;

  // Call the Python script
  const pythonProcess = spawn('python', ['add_receipt.py', name, price, people]);

  // Handle standard output
  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  // Handle Python script errors
  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      return res.status(500).send(`Error occurred: ${data}`);
  });

  // Handle process exit
  pythonProcess.on('close', (code) => {
      if (code === 0) {
          // Successfully added receipt
          res.status(200).json({ message: 'Receipt added successfully' });
      } else {
          res.status(500).json({ message: 'Failed to add receipt' });
      }
  });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});