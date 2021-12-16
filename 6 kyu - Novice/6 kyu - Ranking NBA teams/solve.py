# https://www.codewars.com/kata/5a420163b6cfd7cde5000077/
def nba_cup(result_sheet, to_find):
    win, draw, lose = 0, 0, 0
    scored = 0
    conceded = 0
    teamOneScore = 0
    teamTwoScore = 0
    
    if to_find == "":
        return ""
    else:
        for sheet in result_sheet.split(","):
            if to_find in sheet:
                scores = [s for s in sheet.split() if s.isdigit() or "." in s]  
                if "." in scores[0]:
                    teamOneScore = float(scores[0])
                    return f'Error(float number):{sheet}'
                else:
                    teamOneScore = int(scores[0])
                    
                if "." in scores[1]:
                    teamTwoScore = float(scores[1])
                    return f'Error(float number):{sheet}'
                else:
                    teamTwoScore = int(scores[1])
                    
                data = sheet.split(str(teamOneScore))
                teamOne = data[0].strip()
                teamTwo = data[1].split(str(teamTwoScore))[0].strip()

                if to_find == teamOne:
                    scored += teamOneScore
                    conceded += teamTwoScore
                    if teamOneScore > teamTwoScore:
                        win += 1
                    elif teamOneScore == teamTwoScore:
                        draw += 1
                    else:
                        lose += 1
                elif to_find == teamTwo:
                    scored += teamTwoScore
                    conceded += teamOneScore
                    if teamOneScore < teamTwoScore:
                        win += 1
                    elif teamOneScore == teamTwoScore:
                        draw += 1
                    else:
                        lose += 1

        if scored == 0:
            return f"{to_find}:This team didn't play!"
        else:     
            return f"{to_find}:W={win};D={draw};L={lose};Scored={scored};Conceded={conceded};Points={win*3}"
    