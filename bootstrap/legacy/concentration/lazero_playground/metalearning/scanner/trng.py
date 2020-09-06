import requests
#def trng():
r=requests.get('https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new')
p=r.text
#return p.split("\n")
print(p)
