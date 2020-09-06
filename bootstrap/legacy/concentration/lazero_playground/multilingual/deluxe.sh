#!/bin/bash
service=""
for parameter in "$@"
do
service="$service /$parameter/d; "
done

# echo $service

cd hotfix
ls | sed "$service" > .local-service
