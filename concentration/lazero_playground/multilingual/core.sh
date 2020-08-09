#!/bin/bash
mkdir "$2"
cd $2
curl -k  "https://termbin.com/$1" > download-files.sh
chmod +x download-files.sh
./download-files.sh &
