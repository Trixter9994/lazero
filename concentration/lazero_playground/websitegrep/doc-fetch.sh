#!/bin/bash
man lynx | col -b | cat > docs/lynx.log
man links | col -b | cat > docs/links.log
man w3m | col -b | cat > docs/w3m.log
man elinks | col -b | cat > docs/elinks.log
man links2 | col -b | cat > docs/links2.log
