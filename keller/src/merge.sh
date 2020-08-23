#!/bin/bash
# use global variable.
# heck.
retval=""
function arbitrary(){
	CLO=$(echo "$1" | python3 curl_baidu.py)
#	echo $CLO
	retval=$(curl --header "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" --header "accept-language: zh-CN,zh;q=0.9" --header "cache-control: max-age=0" --header "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" "$CLO")
	#retval=
	#return "hello world"
	# only numeric.
}
IFS=$'\n' read -d '' -r -a lines < SEED
for i in "${lines[@]}";
do
	echo $i
	arbitrary "$i"
#	echo $?
	echo $retval
# and that's your fucking dream.
done
# store it into variables.
