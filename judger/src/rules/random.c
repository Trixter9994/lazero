#include <stdio.h>
#include <seccomp.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

#include "../runner.h"
// the secret is: whitelist + strace -f

int random_seccomp_rules(struct config *_config) {
	// allow them? use root account as example.
//int syscalls_whitelist[]={SCMP_SYS(rt_sigprocmask), SCMP_SYS(getppid), SCMP_SYS(exit_group), SCMP_SYS(getegid), SCMP_SYS(lseek), SCMP_SYS(newfstatat), SCMP_SYS(uname), SCMP_SYS(geteuid), SCMP_SYS(fstat), SCMP_SYS(getrlimit), SCMP_SYS(rt_sigreturn), SCMP_SYS(rt_sigaction), SCMP_SYS(mprotect), SCMP_SYS(clone), SCMP_SYS(getrandom), SCMP_SYS(openat), SCMP_SYS(futex), SCMP_SYS(fcntl), SCMP_SYS(sched_getscheduler), SCMP_SYS(chdir), SCMP_SYS(getgid), SCMP_SYS(wait4), SCMP_SYS(getuid), SCMP_SYS(set_tid_address), SCMP_SYS(ioctl), SCMP_SYS(mmap), SCMP_SYS(execve), SCMP_SYS(close), SCMP_SYS(prctl), SCMP_SYS(munmap), SCMP_SYS(pread64), SCMP_SYS(fstatfs), SCMP_SYS(faccessat), SCMP_SYS(read), SCMP_SYS(sigaltstack), SCMP_SYS(readlinkat), SCMP_SYS(getpgid), SCMP_SYS(nanosleep)
//};
int syscalls_whitelist[]={
	SCMP_SYS(getrlimit), SCMP_SYS(fadvise64), SCMP_SYS(uname), SCMP_SYS(setgid), SCMP_SYS(getgid), SCMP_SYS(geteuid), SCMP_SYS(fstatfs), SCMP_SYS(getrandom), SCMP_SYS(getpgid), SCMP_SYS(getegid), SCMP_SYS(renameat), SCMP_SYS(getdents64), SCMP_SYS(prctl), SCMP_SYS(readlinkat), SCMP_SYS(dup), SCMP_SYS(close), SCMP_SYS(clone), SCMP_SYS(setuid), SCMP_SYS(getcwd), SCMP_SYS(execve), SCMP_SYS(futex), SCMP_SYS(newfstatat), SCMP_SYS(set_tid_address), SCMP_SYS(rt_sigreturn), SCMP_SYS(exit_group), SCMP_SYS(brk), SCMP_SYS(madvise), SCMP_SYS(faccessat), SCMP_SYS(getpid), SCMP_SYS(sched_getscheduler), SCMP_SYS(mmap), SCMP_SYS(munmap), SCMP_SYS(rt_sigprocmask), SCMP_SYS(fchownat), SCMP_SYS(chdir), SCMP_SYS(getuid), SCMP_SYS(mprotect), SCMP_SYS(wait4), SCMP_SYS(sigaltstack), SCMP_SYS(pread64), SCMP_SYS(dup3), SCMP_SYS(read), SCMP_SYS(getppid), SCMP_SYS(fstat), SCMP_SYS(fcntl), SCMP_SYS(lseek), SCMP_SYS(ioctl), SCMP_SYS(setgroups), SCMP_SYS(rt_sigaction),SCMP_SYS(pipe2),SCMP_SYS(socket),SCMP_SYS(socketpair),SCMP_SYS(pselect6),SCMP_SYS(seccomp),SCMP_SYS(setpgid)};
	/*
    int syscalls_whitelist[] = {SCMP_SYS(read), SCMP_SYS(fstat),
	    			SCMP_SYS(dup2),SCMP_SYS(dup),
				SCMP_SYS(umask), SCMP_SYS(flock),
				SCMP_SYS(exit_group),SCMP_SYS(fadvise64),
				SCMP_SYS(dup3),SCMP_SYS(set_robust_list),
				SCMP_SYS(seccomp),SCMP_SYS(arch_prctl),
				SCMP_SYS(connect),SCMP_SYS(getcwd),
	    			SCMP_SYS(readlinkat),SCMP_SYS(faccessat),
				SCMP_SYS(getpgid),SCMP_SYS(prctl),
				SCMP_SYS(getuid),SCMP_SYS(socket),
				SCMP_SYS(stat),SCMP_SYS(pselect6),
				SCMP_SYS(prlimit64),SCMP_SYS(setpgid),
				SCMP_SYS(ioctl),SCMP_SYS(set_tid_address),
				SCMP_SYS(getrandom),SCMP_SYS(openat),
				SCMP_SYS(wait4),SCMP_SYS(getppid),
				SCMP_SYS(getpid),SCMP_SYS(getpgrp),
				SCMP_SYS(getrlimit),SCMP_SYS(geteuid),
				SCMP_SYS(uname),SCMP_SYS(lseek),
				SCMP_SYS(futex),SCMP_SYS(execve),
				SCMP_SYS(getegid),SCMP_SYS(rt_sigaction),
				SCMP_SYS(rt_sigreturn),SCMP_SYS(fstatfs),
				SCMP_SYS(sched_getscheduler),SCMP_SYS(newfstatat),
				SCMP_SYS(getgid),SCMP_SYS(sigaltstack),
				SCMP_SYS(exit_group),SCMP_SYS(rt_sigprocmask),
				SCMP_SYS(pread64),SCMP_SYS(fcntl),
                                SCMP_SYS(mmap), SCMP_SYS(mprotect),
                                SCMP_SYS(munmap), SCMP_SYS(uname),
                                SCMP_SYS(arch_prctl), SCMP_SYS(brk),
                                SCMP_SYS(access), SCMP_SYS(exit_group),
                                SCMP_SYS(close), SCMP_SYS(readlink),
                                SCMP_SYS(sysinfo), SCMP_SYS(lseek),
                                SCMP_SYS(clock_gettime), SCMP_SYS(clone),
				SCMP_SYS(kill), SCMP_SYS(fork),
				SCMP_SYS(ptrace),SCMP_SYS(pause),
				SCMP_SYS(getdents64),SCMP_SYS(lstat),
				SCMP_SYS(select),SCMP_SYS(pipe),
				SCMP_SYS(chdir),SCMP_SYS(statfs),
				SCMP_SYS(vfork), SCMP_SYS(execveat)};*/
    //potential dangerous call: chown, openat, open
    //actually it is pretty enough now.
    //				SCMP_SYS(chown), SCMP_SYS(getdents64),
    int syscalls_whitelist_length = sizeof(syscalls_whitelist) / sizeof(int);
    scmp_filter_ctx ctx = NULL;
    // load seccomp rules
    ctx = seccomp_init(SCMP_ACT_ERRNO(EACCES));
    if (!ctx) {
        return LOAD_SECCOMP_FAILED;
    }
    for (int i = 0; i < syscalls_whitelist_length; i++) {
        if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, syscalls_whitelist[i], 0) != 0) {
            return LOAD_SECCOMP_FAILED;
        }
    }
   /* 
    if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(execve), 1, SCMP_A0(SCMP_CMP_EQ, (scmp_datum_t)(_config->exe_path))) !=0) {
        return LOAD_SECCOMP_FAILED;
    }*/
    // use SCMP_ACT_KILL for socket, python will be killed immediately
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 1, SCMP_CMP(1, SCMP_CMP_MASKED_EQ, O_WRONLY | O_RDWR, 0)) != 0) {
            return LOAD_SECCOMP_FAILED;
        }
        if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 1, SCMP_CMP(2, SCMP_CMP_MASKED_EQ, O_WRONLY | O_RDWR, 0)) != 0) {
            return LOAD_SECCOMP_FAILED;
        }
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 1, SCMP_CMP(2, SCMP_CMP_MASKED_EQ, O_RDWR | O_NONBLOCK, 0)) != 0) {
            return LOAD_SECCOMP_FAILED;
        }/*
	if (seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(openat), 1, SCMP_CMP(2, SCMP_CMP_MASKED_EQ, O_CREAT,O_CREAT)) != 0) {
            return LOAD_SECCOMP_FAILED;
        }*/
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 0))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 1))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 2))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 3))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 4))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 5))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 6))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }
	/*
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 1, SCMP_CMP(0, SCMP_CMP_EQ, 3))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }*/

	const char *path="/dev/tty";
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 1, SCMP_A1(SCMP_CMP_EQ, (scmp_datum_t)(path)))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }
	// that was great. very great.
/*	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 1, SCMP_CMP(0, SCMP_CMP_EQ, AT_FDCWD))!= 0) {
            return LOAD_SECCOMP_FAILED;
        }*/
    if (seccomp_load(ctx) != 0) {
        return LOAD_SECCOMP_FAILED;
    }
    seccomp_release(ctx);
    return 0;
}
