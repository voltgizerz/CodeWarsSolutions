def get_even_numbers(arr)
  arr.select {|num| num % 2 == 0}
end