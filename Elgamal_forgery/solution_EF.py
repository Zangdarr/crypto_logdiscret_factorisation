from client import Server
import random

def XGCD(a,b):
  u = (1, 0) #representation de a
  v = (0, 1) #representation de b

  while b!= 0:
    q,r = divmod(a, b)
    a = b
    b = r
    tmp = (u[0] - q*v[0], u[1] - q*v[1])
    u = v
    v = tmp
  return a, u[0], u[1]

def modinv(a, b):
  g, x, y = XGCD(a,b)
  return x


if __name__ == "__main__" :
    print("Programme Elgamal Forgery ...")
    server = Server("http://pac.bouillaguet.info/TP4/ElGamal-forgery/")

    challenge = server.query("PK/verkyndt")

    p = challenge['p']
    g = challenge['g']
    h = challenge['h']


    print(p)
    print(h)
    print(g)




    print("Fermeture du programme.")
