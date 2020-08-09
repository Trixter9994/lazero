#!/bin/bash
awk '{print "wget \"https://unicode.org/charts/PDF/"$0"\" &"}'  subconscious.sh
