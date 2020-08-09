#!/bin/bash
service=""
for parameter in "$@"
do
service="$service /$parameter/d; "
done
cd hotfix
# echo $service
if [ -f .local-service-copy ]
then
	rm .local-service-copy
fi
#cd hotfix
evaluate="$(pwd)"
ls *.* | sed "$service" > ".local-service"

cp ".local-service" ".local-service-copy"
cd ..

input="hotfix/.local-service"
while IFS= read -r line
do
# as many brackets as possible.
	(x=$(($RANDOM % 1000)); sleep "$(echo "scale=9; $x * 0.0001" | bc )"; ./tower.sh "$evaluate" "$line" ) &
	#(x=$(($RANDOM % 1000)); sleep "$(echo "scale=9; $x * 0.001" | bc )"; ./tower.sh "$evaluate" "$line" & sleep 7; kill $! ) &
#	echo "$line"
done < "$input"

# process the file this time.
cd hotfix
#sed '/termbin.com
sleep 4.5;
sed -i '/https:\/\/termbin.com/!d' .local-service-copy
kill $$
#& '
#'
