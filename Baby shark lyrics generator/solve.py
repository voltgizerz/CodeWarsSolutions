def baby_shark_lyrics():
    l = ["Baby shark", "Mommy shark", "Daddy shark",
         "Grandma shark", "Grandpa shark", "Let's go hunt"]
    t = ''
    for x in range(len(l)):
        for i in range(1, 4):
            t += f"{l[x]}, doo doo doo doo doo doo\n"
        t += f"{l[x]}!\n"
    return t+"Run away,…"
