def divisible_by(numbers, divisor)
    list = []
    for item in numbers
      if item%divisor==0
        list.append(item)
      end
    end
    list
  end