def build_palindrome(s):
  for i in range(len(s)):
      if s + s[:i][::-1] == (s + s[:i][::-1])[::-1]: 
          return s + s[:i][::-1]