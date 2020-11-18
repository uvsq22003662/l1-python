#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné 
    comme jour, heure, minute, seconde.""
    seconde = temps[0] * 86400
    seconde += temps[1] * 3600
    seconde += temps[2] * 60
    seconde += temps[3] 

temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps)) 
