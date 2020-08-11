import random
def get_bingo_card():
    letter=["B","I","N","G","O"]
    card = []
    cnt = 1
    for i in range(5):
        for z in range(5):
            val = letter[i]+str(random.randint(cnt,cnt+14))
            while val in card:
                val = letter[i]+str(random.randint(cnt,cnt+14))
            if letter[i]=="N" and z==2:
                pass
            else:
                card.append(val)
        cnt+=15
    return card


#FOR BEST SOLUTION USE (RANDOM SAMPLE) AND CONCAT THE LIST B, I , N , G , O