var fs = require('fs');
var cheerio = require('cheerio');

fs.readFile('index.html', 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }

  var $ = cheerio.load(data);

  $("a[target|='_blank']").each(function (i, elem) {
    console.log($(this).attr('href'));
  });
});
