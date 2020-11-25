#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné 
    comme jour, heure, minute, seconde."""
    seconde = temps[0] * 86400
    seconde += temps[1] * 3600
    seconde += temps[2] * 60
    seconde += temps[3] 

temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps)) 


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond
     au nombre de seconde passé en argument"""
    jour = seconde // 86400
    reste = reste % 86400
    
    heure = reste // 3600
    reste = reste % 3600
   
    minute = reste // 60
    reste = reste % 60

    return(jour, heure, minute, reste)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", 
                temps[3], "secondes")


#fonction auxiliaire ici

def affichePluriel(mot, nombre):
    if nombre > 0 :
        print(nombre, mot, end ="")
    if nombre > 1 :
        print("s", end="")
    



def afficheTemps(temps):
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichepluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    
afficheTemps((1,0,14,23))   



def demandeTemps():
    jour = -1
    heures = -1
    minutes = -1
    secondes = -1

    while (jour < 0):
        jours = int(input("entrer un nombre de jour"))
    
afficheTemps(demandeTemps())



def demandeTemps():
    jour : -1
    heures : -1
    minutes : -1
    secondes : -1

    while (jour < 0):
        jours = int(input("entrer un nombre de jours"))
    while (heures < 0 or heures >= 24):
        heures = int(input("entrer un nombre d'heures"))
    while (minutes < 0 or >= 60):
        minutes = int(input("entrer un nombre de minutes"))
    while (secondes < 0 or secondes >= 60):
        secondes = int(input("entrer un nombre de secondes"))
    return (jours, heures, minutes, secondes)


while (jours < 0 or heures < 0 or heures >=24 or minutes < 0 or minutes >= 60 or secondes < 60 or secondes >= 60):
    jours = int(input("entrer un nombre de jours"))
    heures = int(input("entrer un nombre d'heures"))
    minutes = int(input("entrer un nombre de minutes"))
    secondes = int(input("entrer un nombre de secondes"))

return (jours, heures, minutes, secondes)


def sommeTemps(temps1 : tuple, temps2: tuple) -> tuple:
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))

afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))

sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))
 

 def sommeTemps(temps1 : tuple, temps2: tuple) -> tuple:
     seconde1 = tempsEnSeconde(temps1)
     seconde2 = tempsEnSeconde(temps2)
     seconde3 = seconde1 + seconde2
     return seconde3
afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


def proportionTemps(temps : tuple, proportion: float) -> tuple :
    secondes = tempsEnseconde(temps)
    secondes = int(secondes * proportion)
    secondeEnTemps(secondes2)
afficheTemps(proportionTemps((2, 0, 36, 0), 0, 2))


def proportionTemps(temps : tuple, proportion: float) -> tuple :
    return secondeEnTemps(int(tempsEnSeconde(temps) * proportion))

afficheTemps(proportionTemps(proportion = 0.2, temps =(2, 36, 0)))



