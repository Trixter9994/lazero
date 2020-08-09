#!/bin/bash
# you could set a config file.
service=""
for parameter in "$@"
do
service="$service /$parameter/d; "
done
cd rockstar/chumble
# echo $service
# make that fucking file!
touch .local-service-copy
touch .local-service
if [ -f .local-service-copy ]
then
	rm .local-service-copy
fi
#cd hotfix
evaluate="$(pwd)"
# list per line
ls -1 *.* | sed "$service" > ".local-service"

cp ".local-service" ".local-service-copy"
cd ..
cd ..
# do it repeatedly

# you shall consider absolute path.
input="rockstar/chumble/.local-service"
while IFS= read -r line
do
# as many brackets as possible.
	(x=$(($RANDOM % 1000)); sleep "$(echo "scale=9; $x * 0.0001" | bc )"; ./tower.sh "$evaluate" "$line" ) &
	#(x=$(($RANDOM % 1000)); sleep "$(echo "scale=9; $x * 0.001" | bc )"; ./tower.sh "$evaluate" "$line" & sleep 7; kill $! ) &
#	echo "$line"
done < "$input"

# this is special.

# process the file this time.
cd rockstar/chumble
#sed '/termbin.com
sleep 4.5;
sed -i '/https:\/\/termbin.com/!d' .local-service-copy
kill $$
#& '
#'
