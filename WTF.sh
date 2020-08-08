#!/bin/bash
git log -100 | grep commit | awk '{if (length($2)==40){ print $2}}' | xargs git show
