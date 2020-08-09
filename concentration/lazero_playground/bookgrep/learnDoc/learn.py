def writer(a,b):
  with open(a,"a+") as f:
    f.write(b+"\n")