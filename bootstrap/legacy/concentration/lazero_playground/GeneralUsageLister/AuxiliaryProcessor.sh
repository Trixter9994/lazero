#!/bin/bash
cat "MainIndexWithIdenticalKeywords.txt" | grep -E "^[^ ,]+" | awk '{print "man " $0 " | col -b | wtf/" $0 ".txt" }'
