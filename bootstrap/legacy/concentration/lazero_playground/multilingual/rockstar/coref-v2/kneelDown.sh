#!/bin/bash
cat POS.log | grep " noun" | grep -E -o "^[^ ]+" > Kneel0.log
cat POS.log | grep " word" | grep -E -o "^[^ ]+" > Kneel1.log
cat POS.log | grep " verb" | grep -E -o "^[^ ]+" > Kneel2.log
