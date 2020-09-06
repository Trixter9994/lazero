//var patt0=new RegExp("https\:\/\/www\.baidu\.com\/s\?")
//var patt1=new RegExp("https\:\/\/www\.baidu\.com\/s\?url=the-best-hings-in-life-are-free");
//fuck you.
//fuck.

var patt1="https://www.baidu.com/s?url=";
var patt2="https://www.baidu.com/s?ul=";
var mess="https://www.baidu.com/s?url=the-best-hings-in-life-are-free";
console.log(mess.includes(patt2)); 
console.log(mess.includes(patt1)); 
//this sucks.
//console.log(mess.(stringObject => stringObject.includes(patt1););)
