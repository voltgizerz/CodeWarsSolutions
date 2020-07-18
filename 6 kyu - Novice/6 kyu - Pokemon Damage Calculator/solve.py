def calculate_damage(your_type, opponent_type, attack, defense):
    dict={
            'firefire': 0.5,
            'grassgrass': 0.5,
            'waterwater': 0.5,
            'electricelectric': 0.5,
            'grassgrass': 0.5,
            'firegrass': 2,
            'grassfire': 0.5,
            'firewater': 0.5,
            'waterfire': 2,
            'fireelectric': 1,
            'electricfire': 1,
            'watergrass': 0.5,
            'grasswater': 2,
            'waterelectric': 0.5,
            'electricwater': 2,
            'grasselectric': 1,
            'electricgrass': 1,
    }
    return 50 * (attack / defense) * dict.get(your_type+opponent_type)