from getFromPickleR import returnWTF
r=returnWTF()
while True:
    i=input("query package name: __END__ to end.\n")
    if i =="__END__":
        break
    try:
        print(r[i])
    except:
        print("not found!")
