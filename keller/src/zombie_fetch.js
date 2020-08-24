const Browser = require('zombie');
const browser = new Browser();
// will have cookie anyway?
// does have shits. but then it will get stuck.
// reuse the cookie once again?
browser.visit('http://www.baidu.com/s?wd=how+to+kill+your+father%0A',function() {
//  const value = browser.getCookie('session');
	const value = browser.source;
  console.log('Cookie', value);
});
