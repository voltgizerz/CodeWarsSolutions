package kata

func Solve(s string, a, b int) string {
	if b < len(s) {
		start := s[:a]
		middle := s[a : b+1]
		end := s[b+1:]
		return start + reverse(middle) + end
	} else {
		start := s[:a]
		middle := s[a:]
		return start + reverse(middle)
	}
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
