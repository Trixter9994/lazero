#!/bin/bash
git log -100 | grep commit | awk '{print $2}' | xargs git show
