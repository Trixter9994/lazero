// #!/usr/bin/nodejs
var express = require('express')
// var crypto = require('crypto');
// not this one.
//var multer = require('multer')
//var upload = multer({dest:''})
function uuidv4() {
  var dt = new Date().getTime()
  var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (
    c
  ) {
    var r = (dt + Math.random() * 16) % 16 | 0
    dt = Math.floor(dt / 16)
    return (c == 'x' ? r : (r & 0x3) | 0x8).toString(16)
  })
  return uuid
}
var app = express()
//app.use(myParser.urlencoded({extended : true,limit:'50mb'}));
//  app.use(bodyParser.json({ limit: '50mb' }))
// return it via web or clipboard.
app.post('/keller', function (req, res) {
  var k = uuidv4()
  // const body = req.body.Body
  // why nothing here?
  //console.log(req.data)
  //console.log(req.file)
  // console.log(req.data)
  res.set('Access-Control-Allow-Origin', '*')
  res.set('Content-Type', 'text/plain')
  res.send(k)
})
// payload too large
// what the heck?
// var server = http.createServer(function (request, response) {
// //   // never read the request?
//   response.writeHead(200, { 'Content-Type': 'text/plain' })
// use some standard outputs, redirect them.
//     console.log("message received.")
//     console.log(request.data)
//     // console.log(request.content)
//     // does not distinguish type?
//     response.end(k)
// })
app.listen(7777)

