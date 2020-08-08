# Dredd (derived from Judger)

[![Build Status](https://travis-ci.org/QingdaoU/Judger.svg?branch=newnew)](https://travis-ci.org/QingdaoU/Judger)

## Judger for OnlineJudge 

[Document](https://docs.onlinejudge.me/#/judger/api)

[JudgeServer](https://github.com/QingdaoU/JudgeServer)

[OnlineJudge](https://github.com/QingdaoU/OnlineJudge)

## Working CLI

```bash
./libjudger.so --exe_path=$(which bash) --seccomp_rule_name="randomfuck"

./libjudger.so --exe_path=/data/data/com.termux/files/usr/bin/bash --input_path=/proc/self/fd/0 --output_path=/proc/self/fd/1 --error_path=/proc/self/fd/2 --uid=0 --gid=0 --seccomp_rule_name="random"

./libjudger.so --exe_path=$(which bash) --input_path=/proc/self/fd/0 --output_path=/proc/self/fd/1 --error_path=/proc/self/fd/2 --uid=0 --gid=0 --seccomp_rule_name="random"
```

## Reminder

The [libseccomp](https://github.com/seccomp/libseccomp) is different around different platforms. Separate changes are according to the systemcall table, specified under [src/syscalls.csv](https://github.com/seccomp/libseccomp/blob/master/src/syscalls.csv).

## Compilation Tips

Custom patches applied. However, in order to compile under Termux directly, you need to modify the include/bits/ioctl.h to disable buggy macro.

Maybe it's by mistakenly placing part of Android NDK into the include folder. Anyway libseccomp package is needed, while custom pthread workaround is applied.
