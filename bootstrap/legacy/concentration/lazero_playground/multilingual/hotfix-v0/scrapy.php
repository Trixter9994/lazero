<?php
function  curl_post_302($url) {
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_VERBOSE, true);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_NOBODY, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 20);
curl_setopt($ch, CURLOPT_AUTOREFERER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
$ret = curl_exec($ch);
$info = curl_getinfo($ch);
$retURL = $info['url'];
curl_close($ch);
return $retURL;
          }
$fuckingfucker="http://www.baidu.com/link?url=mQRln1LKWUncYQMSCUu01Uq09GtFVObdNqylQdFpk3ebBca2mr5AzXeNyG31ljYB3dW5Ke9vJ2nPVEZ08vicwxSK0mVBg5KQWHUMXdqZcs3";
$super_redirect=curl_post_302($fuckingfucker);
echo $super_redirect;
// you fuck!
// you are already there!
// fuck just give me the fucking link!
?>
