package kata

func WordsToMarks(s string) int {
	count := 0
	for i := 0; i < len(s); i++ {
		count += int(rune(s[i]) - 96)
	}
	return count
}
