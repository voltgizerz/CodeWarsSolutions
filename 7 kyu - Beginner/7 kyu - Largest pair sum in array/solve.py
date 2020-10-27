def largest_pair_sum(numbers): 
  numbers.sort(reverse=True)
  return numbers[0] + numbers[1]