# https://www.codewars.com/kata/567501aec64b81e252000003/
import math
def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    
    if l*w*h == 0:
        return "zero"
    else:
        largeWalls = (((l * h) * 2) + (( w * h ) * 2))
        return numbers[math.ceil((largeWalls + (largeWalls * 0.15)) / (0.52 * 10))]


