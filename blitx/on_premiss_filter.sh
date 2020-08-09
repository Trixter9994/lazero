#!/bin/bash
get_checked(){
	# parameters are not named.
	echo $1
}
res0=$(echo $(./check_mount.sh | grep -i cpu | awk '{print $2}'))
IFS=' '
read -ra ADDR <<<"$res0"
ARRAY=()
for i in "${ADDR[@]}";
do
	target_string="cpu.cfs_quota_us"
	echo_string=$( get_checked $(ls $i -1 | grep -i $target_string) )
	if [ "$target_string" == "$echo_string" ]; then
		# use this directory. append to candidate list.
		ARRAY+=$i
	else
		:
		# this is when things going philosophical.
		# the null command.
	fi
#	echo "delimiter"
# check if it has the thing.
# then make the subfolder. you might want to do it. any python bindings on cgroups?
# worst day of my life.
done

candidates=${#ARRAY[@]}
#candidates=0
if [ $candidates -lt 1 ]; then
	echo "No candy"
else
	echo "yes man"
fi
#for i in "${ARRAY[@]}"
#do
#	echo $i
#done
