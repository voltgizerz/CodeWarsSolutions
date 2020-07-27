dict = {
       0: "I love you",
       1: "a little",
       2: "a lot",
       3: "passionately",
       4: "madly",
       5: "not at all",
}
def how_much_i_love_you(nb_petals):
    return dict.get((nb_petals-1)%6) 