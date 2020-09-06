const util = require('util');
const exec = util.promisify(require('child_process').exec);

async function manipulate(input) {
	var command="curl -b baidu.cookies http://www.baidu.com/s?word="+input;
  const { stdout, stderr } = await exec(command);
//	console.log(stdout);
//	console.log(stdout1);
//  console.log('stderr:', stderr);
	return stdout;
};
var fuckinglist0=new Promise (function (){let hometown=manipulate("python");
return hometown;
});

Promise.all([fuckinglist0]).then(function(values) {
  console.log(values);
});
//const {wtf0,wtf1}=await fuckinglist;
//console.log(wtf0+wtf1);
