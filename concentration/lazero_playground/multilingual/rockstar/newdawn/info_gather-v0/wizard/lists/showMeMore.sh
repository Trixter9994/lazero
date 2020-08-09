#!/bin/bash
ls  -1 make* | awk '{print"python3 "$0}' > newShit.sh
# this IS not GNU sed.
sed -i '1i #!/bin/bash' newShit.sh

chmod +x newShit.sh
