#!/bin/bash
./cloudnine.sh index.html
sleep 2;
cat hotfix/.local-service-copy | nc termbin.com 9999
kill $$
