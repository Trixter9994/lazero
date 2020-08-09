#!/bin/bash
aria2c --load-cookies=baidu.cookies --max-connection-per-server=4 --min-split-size=1M "http://www.baidu.com/s?word=java+pyton" -o main.log
