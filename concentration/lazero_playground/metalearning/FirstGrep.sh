#!/bin/bash
cat WordsExample/0.log | grep -E -o "^[^。]+(。)" | cat > 0.summary
