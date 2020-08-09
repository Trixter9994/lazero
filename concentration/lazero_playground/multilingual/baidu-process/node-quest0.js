const http = require('http');
var k="lisp multithreading arm64"
http.get('http://www.baidu.com/s?word='+encodeURIComponent(k), (resp) => {
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
