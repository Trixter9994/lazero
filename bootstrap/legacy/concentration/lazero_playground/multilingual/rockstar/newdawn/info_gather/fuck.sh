#!/bin/bash
var=$(pwd)
cd /data/data/com.termux/files/home/lazer/multilingual/hotfix-v1
lua marine.lua 0 bing search api  > $var"/supercube.txt"
