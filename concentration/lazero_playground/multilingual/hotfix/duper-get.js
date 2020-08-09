//var fs = require('fs');
//IT FUCKING WORKS!
//FUCKING FUCK!
var cheerio = require('cheerio');
//const axios = require('axios');  
var content=process.argv[2];               // remember to write things here.  
var p = encodeURIComponent(content);
var n=0;   
var axios = require('axios');              

//var data0="";
//var data1="";

axios.all([                                  axios.get('http://www.baidu.com/s?pn='+n+"0"+"&word="+p),                             axios.get('http://www.baidu.com/s?pn='+(n+1)+"0"+"&word="+p)                        ]).then(axios.spread((response1, response2) => {                              
var $ = cheerio.load(response1.data);
//console.log(data0);
  $("a[target|='_blank']").each(function (i, elem) {
    console.log($(this).attr('href'));
  });

 $ = cheerio.load(response2.data);                                                          $("a[target|='_blank']").each(function (i, elem) {                                      console.log($(this).attr('href'));       });

	//response1.data.pipe(data0); 
//	console.log(response1.data);
	//	did you forget that this fucking thing is async?
//response2.data.pipe(data1);
})).catch(error => {                         console.log(error);                      });

/*fs.readFile('index.html', 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }*/
// wow this is awesome.
	// but i need a direct approach.

  
