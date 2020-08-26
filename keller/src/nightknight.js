//use nodejs this time.
const Nightmare = require('nightmare')
//const nightmare = Nightmare({ show: true,switches:{'ignore-certificate-errors': true}})
const nightmare = Nightmare({show:true});
// not running.
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

nightmare.goto('https://www.baidu.com').evaluate(() => {return document.title;}).end().then((title) => {console.log(title);})

async function santa(){await sleep(10);}
santa();
