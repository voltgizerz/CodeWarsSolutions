def is_vow(a)
    replacements = {
      117 => 'u',
      101 => 'e',
      105 => 'i',
      111 => 'o',
      97 => 'a',
    }
    array = a.map do |e |
        replacements.fetch(e, e)
    end
  end