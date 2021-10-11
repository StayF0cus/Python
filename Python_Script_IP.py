import platform
import os
from sys import argv
from os import listdir




#On verifie le nombre d'arguments
if len(argv) == 2:
    #Si le parametre est -h on explique a quoi va servir le programme
    if argv[1] == "-h":
        print("Le programme va servir à récuperer les ip selon les OS")
    else :
        print("Vos arguments ne sont pas bon")

#On passe au programme
else:
    systeme = platform.system()  # Récupération du nom du système
    version = platform.release()  # Récupération de la version du système
    print("Le système d'exploitation est : %s et la version est : %s" % (systeme, version))

    #Test pour avoir les différentes informations celon Windows / Linux / MacOs
    if systeme == "Windows":
        print("Nous somme sur %s" %(systeme))

        print('\n******************************************\n')

        try:
            # On fait la commande pour avoir la liste des ip et on met le résultat dans un fichier txt
            os.system('ipconfig > ip.txt')

        #Si la création n'a pas fonctionné on sort
        except:
            print("probleme dans la création de fichier")
            exit()

        #On verifie si le fichier est présent
        if 'ip.txt' in listdir():
            print("le fichier est présent ")

        else:
            print("le fichier n'est pas présent")
            exit()

        print('\n******************************************\n')

        # On ouvre le fichier txt en mode lecture et on récupere les lignes, on les split et on prend la bonne valeur
        with open('ip.txt', 'r') as f1:
            print("Voici les IPv4")
            for line in f1.readlines():
                line = line.split(' ')
                if 'IPv4.' in line:
                    print(line[18])

            print('\n******************************************\n')

    elif systeme == "Linux":
        print("Nous somme sur %s" % (systeme))

        print('\n******************************************\n')

        try:
            # On fait la commande pour avoir la liste des ip et on met le résultat dans un fichier txt
            os.system('ifconfig > ip.txt')
        except:
            print("probleme dans la création de fichier")
            exit()

        # On verifie si le fichier est présent
        if 'ip.txt' in listdir():
            print("le fichier est présent ")

        else:
            print("le fichier n'est pas présent")
            exit()

        print('\n******************************************\n')

        # On ouvre le fichier txt en mode lecture et on récupere les lignes, on les split et on prend la bonne valeur
        with open('ip.txt', 'r') as f1:
            print("Voici les IPv4")
            for line in f1.readlines():
                line = line.split(' ')
                if 'inet.' in line:
                    print(line[9])

        print('\n******************************************\n')

    elif systeme == "Darwin":
        print("Nous somme sur %s" % (systeme))

        print('\n******************************************\n')

        try:
            # On fait la commande pour avoir la liste des ip et on met le résultat dans un fichier txt
            os.system('ifconfig > ip.txt')
        except:
            print("probleme dans la création de fichier")
            exit()

        # On verifie si le fichier est présent
        if 'ip.txt' in listdir():
            print("le fichier est présent ")

        else:
            print("le fichier n'est pas présent")
            exit()

        print('\n******************************************\n')

        # On ouvre le fichier txt en mode lecture et on récupere les lignes, on les split et on prend la bonne valeur
        with open('ip.txt', 'r') as f1:
            print("Voici les IPv4")
            for line in f1.readlines():
                line = line.split(' ')
                if 'inet.' in line:
                    print(line[9])

        print('\n******************************************\n')

    #Si on ne detecte pas d'os on sort
    else:
        print("Probleme dans le systeme d'exploitation")