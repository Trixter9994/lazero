#!/bin/bash
cd "$1"
#name="$1"
superlink="$(cat $2 | nc termbin.com 9999)"
#superlink="cat local.js | nc termbin.com 9999"
#superlink="$superlink"
sed -i "/$2/d" "$1/.local-service-copy"
nextlink="curl -k $superlink > $2 &"
echo $nextlink >> "$1/.local-service-copy"
#kill $!
kill $$
