import winsound
from win32com.client import Dispatch
# import os
# import argparse
# ?
speak = Dispatch("SAPI.SpVoice")


def waiter(x):
    speak.Speak(x)


def theBeep(r0, r1, r2):
    d = 3
    frequency = int((32767-37)*r0+37)  # Set Frequency To 2500 Hertz
    duration = int(1+450 * r1)  # Set Duration To 1000 ms == 1 second
    d0 = int(d*r2)
    for x in range(d):
        # has separation
        winsound.Beep(frequency, duration)

# # simple shit.
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser("Sound logging module.")
#     group = parser.add_mutually_exclusive_group()
#     group.add_argument("-s", type=str, help="Text logging.")
#     # parser.add_argument("x",)
#     group.add_argument("-i", type=int, help="Times of beeping.")
#     args = parser.parse_args()
#     s0, i0 = args.s, args.i
#     # print(s0,i0)
#     # assert s0 in [0, 1]
#     if s0 != None:
#         waiter(s0)
#     else:
#         theBeep(i0)
#     # if s0 == 0:
#     #   waiter(i)
#     # else:
#     #   theBeep()
# # def getter(a, b):
# #   if a:
# #     os.popen()
