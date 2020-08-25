const Browser = require('zombie');
function bfunc(a){
	return 'http://www.baidu.com/s'+a;
}
const browser = new Browser();
// will have cookie anyway?
// does have shits. but then it will get stuck.
// reuse the cookie once again?
function bvisit(a){
browser.visit(bfunc(a),function() {
//  const value = browser.getCookie('session');
	const value = browser.source;
  console.log('Cookie', value);
});
}
