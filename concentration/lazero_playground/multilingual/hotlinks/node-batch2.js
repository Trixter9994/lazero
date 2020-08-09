//const axios = require('axios');
var content=process.argv[2];                      var p = encodeURIComponent(content);
var n=0;
var axios = require('axios');
// three in a batch.
axios.all([
  axios.get('http://www.baidu.com/s?pn='+n+"0"+"&word="+p),
  axios.get('http://www.baidu.com/s?pn='+(n+1)+"0"+"&word="+p),
axios.get('http://www.baidu.com/s?pn='+(n+2)+"0"+"&word="+p)
]).then(axios.spread((response1, response2,response3) => {
  console.log(response1.data);
  console.log(response2.data);
console.log(response3.data);
//console.log(response4.data);
})).catch(error => {
  console.log(error);
});
