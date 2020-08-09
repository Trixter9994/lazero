from dbM import showN
while True:
    i=input("query package name: __END__ to end.\n")
    if i =="__END__":
        break
    try:
        print(showN("projects",i))
    except:
        print("not found!")
