a="Kneel"
# I wanna to make a template.

supertemp=(lambda  fstring,strings,spliter: list(filter((lambda x:x!=fstring),strings.split(spliter))))

# to create it from nothing.
with open("faith.log","w+") as faith:
    for x in range(3):
        with open(a+str(x)+".log","r") as ontology:
            #meta=list(filter((lambda x: x!=""),ontology.read().split("\n")))
            meta=supertemp("",ontology.read(),"\n")
            for y in meta:
                faith.write(y+" ")
            faith.write("\n")
        # we are the machine.
        # with the trailing newline.
    faith.close()
