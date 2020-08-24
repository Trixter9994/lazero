var http = require('http');
    var server = http.createServer ( function(request,response){

    response.writeHead(200,{"Content-Type":"text/plain"});
    if(request.method == "GET")
        {
            response.end("received GET request.")
        }
    else if(request.method == "POST")
        {//console.log(request.data);
		request.on('data', function(data) {
      //body += data
      console.log('Partial body: ' , data)
    })
    request.on('end', function() {
      console.log('Body End')
      response.writeHead(200, {'Content-Type': 'text/html'})
      response.end('post received')
    })
        }
    else
        {
            response.end("Undefined request .");
        }
});
//arbitrary path.
server.listen(7777);
console.log("Server running on port 7777");
