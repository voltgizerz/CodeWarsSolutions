class Array
    def square
      self.map {|num| num ** 2}
    end
    
    def cube
      self.map {|num| num ** 3}
    end
    
    def sum
      self.compact.inject(:+)
    end
    
    def average
      self.compact.inject(:+) / self.size
    end
    
    def even
      self.select(&:even?)
    end
    
    def odd
      self.select(&:odd?)
    end
  
    # now fill in the rest
  end