const { exec } = require('child_process');
exec('lua luarock.lua "http://www.baidu.com/s?word=java+python" ', (err, stdout, stderr) => {
  if (err) {
    // node couldn't execute the command
    return;
  }

  // the *entire* stdout and stderr (buffered)
  console.log(`stdout: ${stdout}`);
  //console.log(`stderr: ${stderr}`);
	//the stderr is for progress this time.
	//it is still predelayed.
});
