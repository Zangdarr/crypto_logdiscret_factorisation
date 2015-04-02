from client import Server

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
