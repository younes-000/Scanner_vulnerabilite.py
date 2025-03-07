# les libs
import requests
import re
import os
import socket

# on doit faire un scanner 


def myscanner(cible,ports):
    print("Scanner en cours sur la cible: ",cible)
    for port in ports: # on parcourt les ports
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on crée un socket permettant de se connecter à un serveur
        sock.settimeout(2) # on fixe un timeout de 2 secondes ça sert à rien d'attendre plus longtemps
        code = sock.connect_ex((cible,port)) # on essaye de se connecter au serveur
        if code == 0:
            print("Port ouvert: ",port)
        else:
            print("Port fermé: ",port)

# on va scanner le site web de la NASA
cible = "" # ici on met le site à scanner
ports = [80,443,21,22,23,25,53,110,443,3389,8080] # on va scanner les ports les plus connus
myscanner(cible,ports) # on lance le scanner

