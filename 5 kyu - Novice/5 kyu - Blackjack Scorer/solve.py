def score_hand(cards):
    cards_points ={'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    cardsNumeric= [x for x in cards if x.isnumeric()]
    cardsNumeric.extend(sorted([x for x in cards if x.isalpha()],reverse=True))
    sum = 0
    for i in cardsNumeric:
        if sum==10 and len(cardsNumeric)>2 and i=='A':
            sum+= 1
        elif sum+cards_points.get(i)>21 and i=='A' :
            sum+= 1
        else:
            sum+= cards_points.get(i)
    return sum