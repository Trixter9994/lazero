const http = require('http');
// var iconv = require('iconv');  
content=process.argv[2];                      var p = encodeURIComponent(content);          //iconv.encode(content, 'gb2312');    
//console.log(p);
//is this thing really needed?
http.get('http://www.baidu.com/s?word='+p, (resp) => {
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
