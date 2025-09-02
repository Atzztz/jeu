import random
r = random.randint(1, 10)
tantative = 3 
print("Bienvenue dans le jeu du nombre devinette !")
print("Vous avez 3 tentatives pour deviner le nombre entre 1 et 10.")
while tantative > 0:
    user = int(input("Entrez votre nombre : "))
    if user == r:
        print(f"Félicitations ! Vous avez deviné le bon nombre.{r}")
        break
    elif user < r:
        print("C'est plus grand !")
    else:
        print("C'est plus petit !")
    tantative -= 1
    print(f"Il vous reste {tantative} tentatives.")
if tantative == 0:
    print(f"Vous avez épuisé vos tentatives. Le nombre était 🤣 {r}.")