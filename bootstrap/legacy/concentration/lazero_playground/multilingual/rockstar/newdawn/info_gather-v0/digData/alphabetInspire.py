# Keep the pattern inside a list.
with open("standard_pattern.log","r") as fuck:
    fuck0=list(filter((lambda x:x!=""),fuck.read().split("\n")))
    print(fuck0)
