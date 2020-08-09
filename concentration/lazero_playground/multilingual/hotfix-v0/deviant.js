var fs = require('fs');
var cheerio = require('cheerio');
// our brand new regexp!
// fuck you regexp!
//var patt1=new RegExp("e");
// asshole!
const patt0="http://www.baidu.com/link?url=";

// we've got the brand new fucking <string_object_name>.includes(<substring_object_name>) method!
// fuck you asshole!
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
// this thing is merely a improvement over the local thing.
// make sure you have the real experiment.
fs.readFile('index.html', 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }

  var $ = cheerio.load(data);
// does it contain the thing?
	// fucking army!
	// i still think that little esc thing is necessary for the shit.
  $("h3[class~='t']").each(function (i, elem) {// this fucking works
	  // do not even think of other shits.
	  // save your mother fucking time.
//	  var poker = $(this).prop("tagName").toLowerCase();
//	  console.log(poker);
	  var poker=$(":first-child",$(this)).attr("href");
//	  console.log(rock);
//	  document.write(patt1.test("The best things in life are free")); 
//this is just for reference
	  if (poker.includes(patt0)){
	// the real thing.
		  //var rock=$(this);
		  console.log("----------------");
		  console.log(poker);
	console.log($(this).text());
// keep these lines in some sort of ioop.
	  var rock=$(this).next();
// jQuery got this version of nextSibling() as next()
// this is the premise.
	if (rock.attr("class").includes("c-abstract")==true)
		  {console.log(rock.text());}
		  else
		  {console.log($(":first-child",$(":first-child",$(rock)).next()).text());
			  //r u kidding me?
	//next sibling?
};

	  };
  });
});
// time to make it simple.
// i do not think that you need any kind of ads.
// simple stuff works the best.


