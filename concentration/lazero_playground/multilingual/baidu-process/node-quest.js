const http = require('http');

http.get('http://www.baidu.com/s?word=%E5%A4%AE%E8%A7%86%E6%9A%82%E5%81%9CNBA%E8%BD%AC%E6%92%AD', (resp) => {
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
