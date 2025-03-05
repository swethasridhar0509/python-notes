import random 

while True:
    health = enemy_health = 5
    actions = ("attack", "run")

    while health > 0 and enemy_health > 0:
        action = input("Choose Action (attack/run): ").lower()
        if action not in actions:
            print("Choose the correct action")
            continue 
        else:
            if action == "run":
                health = 0
                break
            else:
                enemy_health -= 1
                print(f"You attacked! Enemy - {enemy_health} | You - {health}")
                enemy_choice = random.choice([True, False])
                if enemy_choice:
                    health -= 1
                    print(f"Enemy Attacked! Enemy - {enemy_health} | You - {health}")
                    
    print("You Won!" if health > enemy_health else "You Lost!")

    if input("Do you want to play again (y/n)? ").strip().lower() == "n":
        break