const base64="hello world";
var http = new XMLHttpRequest();
http.open("POST", "http://localhost:7777/phantom_render", true);
//	  http.setRequestHeader("Content-type","application/png");
http.send(base64);
	  //  string. can be other things. make a post request. fetch.
	  /*var data= new FormData();
	  data.append("screenshot",data)*/
	  /*fetch("http://localhost:7777/phantom_render",{
		  method:"POST",
		  body:base64
	  });*/
	  // send it into other things.
// this one is called the webkit.
// no websecurity.
