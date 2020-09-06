#shade0="     set: А, а, Б, б, В, в, Г, г, Ґ, ґ, Д, д, Е, е, Є, є, Ж, ж, З, з, И, и, І, і, Ї, ї, Й, й, К, к, Л, л, М, м, Н, н, О, о, П, п, Р, р, С, с, Т, т, У, у, Ф, ф, Х, х, Ц, ц, Ч, ч, Ш, ш, Щ, щ, Ь, ь, Ю, ю, Я, я"

def neuron(shade,rk,rho):
    horror=list(shade)
    crystal=[]
    if len(horror)>rk:
        for r,k in enumerate(horror):
            if r>rk and r%3==rho:
                crystal.append([k,ord(k)])
    else:
        pass
            # use the index only.
    return crystal

#print(neuron(shade0,9,1))
