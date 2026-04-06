const http = require('http');

const PORT = 1245;
const HOST = 'localhost';

// Create the server
const app = http.createServer((req, res) => {
  // Set the response header to plain text
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  
  // Send the body content
  res.end('Hello Holberton School!');
});

// Start listening on port 1245
app.listen(PORT, HOST);

// Export the app variable
module.exports = app;
