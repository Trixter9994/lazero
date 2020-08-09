#!/bin/bash
cat makeDatabase.py makeGroupingDatabase.py | grep -E -o "CREATE TABLE [^ ]+" | grep -E -o "[^ ]+$" > simpleDeduction.txt
