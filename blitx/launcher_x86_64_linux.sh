#!/bin/bash
cd bin/linux/x86_64
./libjudger.so --exe_path=$(which bash) --seccomp_rule_name="randomfuck" --max_cpu_time=500 --max_real_time=5000 --max_memory=14213120 --max_stack=500000 --max_process_number=2
