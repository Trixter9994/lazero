var fs = require('fs');
var cheerio = require('cheerio');
/*function range(size:number, startAt:number = 0):ReadonlyArray<number> {
    return [...Array(size).keys()].map(i => i + startAt);
}
function range(size, startAt) {
    return [...Array(size).keys()].map(i => i + startAt);
}
// this will only make the step equal to one.
function mobious(numberStart,numberEnd){
	var list=range(1+numberEnd-numberStart,numberStart);
	list=list.map(i => 'div[id="'+i+'"], ');
	var s="";
	for (var i = 0; i < list.length; i++) { 
  s+= list[i] ;
}
s = s.slice(0,-2);
console.log(s);
return s;
}*/
// you had better create a function to utilize the selector.
// anyway don't believe in anything magical about regex selector here.
// if you want that go for python instead or something called lua.

// use something apart from this.

fs.readFile('index.html', 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }

  var $ = cheerio.load(data);

  $("h3[class*='c-title'], div[class*='c-abstract']").each(function (i, elem) {// this fucking works
	  var poker = $(this).prop("tagName").toLowerCase();
	  console.log(poker);
	  if (poker =="h3"){console.log($(":first-child",$(this)).attr("href"));};
	  // prop() is not avaliable here.
	  console.log($(this).text());

  });
});


