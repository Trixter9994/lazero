var axios=require("axios");
var link="https://www.baidu.com/link?url=mQRln1LKWUncYQMSCUu01Uq09GtFVObdNqylQdFpk3ebBca2mr5AzXeNyG31ljYB3dW5Ke9vJ2nPVEZ08vicwxSK0mVBg5KQWHUMXdqZcs3"
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
//sleep well you fucking bitch!
var source="";
axios.get(link).then(response => (
	console.log(response.responseUrl)
)).catch(function (error) { 
// 请求失败处理
	// this won't work.
	// this fucking works!
	// fucking fucked!
//console.log(error.request.res.responseUrl);
	//make some fucking deadlock.
//while (source==""){
//sleep(1).then(() => {
    // 这里写sleep之后需要去做的事情
console.log(error.request.res.responseUrl);

//console.log(source);
//})
//}
});
