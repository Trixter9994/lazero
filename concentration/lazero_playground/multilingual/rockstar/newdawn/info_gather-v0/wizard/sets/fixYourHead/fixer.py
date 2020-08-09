with open("fixedExample.log","w+") as ap:
    with open("exampleToBeFixed.log","r") as ad:
        shit=0
        for abo in ad.readlines():
            print (shit)
            print(abo)
            if shit == 1:
                #shit+=1
                abo = abo.replace("need", "need not")
#                print(abo)
                ap.write(abo)
            else:
                ap.write(abo)
            shit+=1
