import fcntl
import sys
import termios
# must make the overall thing deterministic.
# https://unix.stackexchange.com/questions/48103/construct-a-command-by-putting-a-string-into-a-tty/48221
# i really have to tear it off to get the essense of machine.
# it is unknown numbers. just like that.
# what the fuck. all the same.
# what about some sort of screen command?
# xdotool
# expect??
# quit it.
# that really works.
# but it is still hard to get content from windows???
# how to get the thing?
# c="echo hello world\n"
# need separate input?
# yes. so it is hard to get the real thing.
# 
# but how do you quit it? blind shot? or that cpan thing?
# c="\x02d"
c="ls\n"
# but I can force it to execute something to dump content!
with open('/dev/pts/8', 'w') as fd:
    # print(type(fd))
    # with open('/proc/71043/fd/0', 'w') as fd:
    # for char in "\x01d":
    for char in c:
        fcntl.ioctl(fd, termios.TIOCSTI, char)
        # it works. you can do some util.
        # io control on file descripters? what about windows?
        # forget about it. all we need is concentration.
        # ls | rev | cut -d'.' -f1 | rev |sort |uniq -c