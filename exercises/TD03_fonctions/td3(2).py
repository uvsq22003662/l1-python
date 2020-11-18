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


