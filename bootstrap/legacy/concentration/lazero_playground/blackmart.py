from utl import get_subscriber

g = get_subscriber("127.0.0.7", "2000", "")

while True:
    g0 = g.recv_string()
    print(g0)
