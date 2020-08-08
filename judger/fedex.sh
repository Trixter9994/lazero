#!/bin/bash
sudo rm /var/lib/rpm/__db.*
cd /var/cache/yum
sudo rm -rf *
yum clean all
yum update
sudo rm /var/lib/rpm/.rpm.lock
