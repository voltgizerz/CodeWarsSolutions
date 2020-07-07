def song_decoder(song):
    return " ".join([ele for ele in song.split("WUB") if ele.strip()])