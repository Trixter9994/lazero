// var iconv = require('iconv');
content=process.argv[2];
var p = encodeURIComponent(content);
//iconv.encode(content, 'gb2312');
console.log(p);
