#!/bin/bash
cd hotfix
superlink="$(cat local.js | nc termbin.com 9999)"
echo $superlink &
