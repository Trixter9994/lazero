<?php
//$url = "http://www.baidu.com/link?url=nS2MGJqjJ4zBBpC8yDF8xDh8vibi1lVeE7gGr9UONBu";
//save the thread or not?
//now we do not consider nothing.
//just use every fucking thread.
$url=$argv[1];
// this was the wrong fucking thing
// $argv instead of $args!
// fuck you! 
$info = parse_url($url);
$fp = fsockopen($info['host'], 80,$errno, $errstr, 30);
fputs($fp,"GET {$info['path']}?{$info['query']} HTTP/1.1\r\n");
fputs($fp, "Host: {$info['host']}\r\n");
fputs($fp, "Connection: close\r\n\r\n");
$rewrite = '';
while(!feof($fp)) {
    $line = fgets($fp);
    if($line != "\r\n" ) {
        if(strpos($line,'Location:') !== false) {
            $rewrite = str_replace(array("\r","\n","Location: "),'',$line);
        }
    }else {
        break;
    }
}
//is this the fucking way to combine strings?
//$rewrite="$rewrite\n";
//shit this fucking works.
echo "$rewrite"; //结果显示：string(22) "http://www.google.com/"
//this fuck is good.
//you should not end this without a fucking return.
//except when combined with the fucking lua.
?>
