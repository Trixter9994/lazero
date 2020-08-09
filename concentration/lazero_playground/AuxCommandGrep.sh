#!/bin/bash
awk '{print $0 " -h" " | cat > Aux0/" $0 ".txt" }' "CommandGrepMainIndex.txt" | cat > Aux0.sh
awk '{print $0 " --help" " | cat > Aux1/" $0 ".txt" }' "CommandGrepMainIndex.txt" | cat > Aux1.sh
