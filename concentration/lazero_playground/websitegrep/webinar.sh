#!/bin/sh
ABCL_JAR=/opt/abcl/abcl.jar	# Use your own path here.
JAVA=$(which java)
ABCL="$JAVA -server -Xrs -cp $ABCL_JAR org.armedbear.lisp.Main"
if [ $# -eq 0 ]; then
	exec rlwrap -b "[]()'\" " --remember -c -f ~/.abcl_completions \
				  -H ~/.abcl_history -s 1000000 $ABCL
else
	exec $ABCL "$@"
fi