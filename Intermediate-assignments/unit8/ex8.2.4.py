def sort_anagrams(list_of_strings):
    anagram_lists = []
    while len(list_of_strings) > 0:
        anagram_word = list_of_strings.pop(0)
        anagram = [anagram_word]
        i = 0
        while i < len(list_of_strings):
            if sorted(list(list_of_strings[i])) == sorted(list(anagram_word)):
                anagram.append(list_of_strings.pop(i))
            else:
                i += 1
        anagram_lists.append(anagram)
    return anagram_lists
