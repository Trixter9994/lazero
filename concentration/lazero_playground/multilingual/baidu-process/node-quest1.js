const http = require('http');

// max rn is 50 or 100
// however this is fucked.
http.get('http://www.baidu.com/s?word=java?pn=20', (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    console.log(data);
  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});
