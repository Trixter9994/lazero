//const axios = require('axios');
var content=process.argv[2];                      var p = encodeURIComponent(content);
var n=0;
var axios = require('axios');

axios.all([
  axios.get('http://www.baidu.com/s?pn='+n+"0"+"&word="+p),
  axios.get('http://www.baidu.com/s?pn='+(n+1)+"0"+"&word="+p),axios.get('http://www.baidu.com/s?word='+p+"&pn="+(n+2)+"0"),                                       axios.get('http://www.baidu.com/s?word='+p+"&pn="+(n+3)+"0"),axios.get('http://www.baidu.com/s?word='+p+"&pn="+(n+4)+"0"),                                       axios.get('http://www.baidu.com/s?word='+p+"&pn="+(n+5)+"0"),axios.get('http://www.baidu.com/s?word='+p+"&pn="+(6+n)+"0"),                                       axios.get('http://www.baidu.com/s?word='+p+"&pn="+(n+7)+"0"),axios.get('http://www.baidu.com/s?word='+p+"&pn="+(8+n)+"0"),                                       axios.get('http://www.baidu.com/s?word='+p+"&pn="+(n+9)+"0")
]).then(axios.spread((response1, response2,response3,response4,response5,response6,response7,response8,response9,response10) => {
  console.log(response1.data);
  console.log(response2.data);
console.log(response3.data);
console.log(response4.data);
console.log(response5.data); 
console.log(response6.data); 
console.log(response7.data); 
console.log(response8.data);
console.log(response9.data);  
console.log(response10.data); 
})).catch(error => {
  console.log(error);
});
