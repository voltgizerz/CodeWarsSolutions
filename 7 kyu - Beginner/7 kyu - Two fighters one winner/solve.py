def declare_winner(fighter1, fighter2, first_attacker):
    while fighter1.health > 0 and fighter2.health > 0:
         fighter2.health -= fighter1.damage_per_attack
         fighter1.health -= fighter2.damage_per_attack

    if fighter1.health <= 0 and fighter2.health <= 0:
       return first_attacker
    elif fighter1.health <= 0:
       return fighter2.name
    else:
       return fighter1.name