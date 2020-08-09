import base64
a = [1, 2, 3, 4]
a0 = str(a).encode("utf-8")
a1 = base64.b64encode(a0)
# a = "WzEsIDIsIDMsIDRd"
a2=a1.decode()
# a2 = base64.b64decode(a)
# a4 = a2.decode("utf-8")
# a3 = eval(a4)
# well, you still have some use!
# print(a, a0, a1, a2, a4, a3)
# print(a, a2, a4, a3)
print(a2)
# you are experiments.
# is it binary?
# binary shit?
