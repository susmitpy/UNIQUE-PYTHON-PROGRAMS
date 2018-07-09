"""

This question was asked on Hackerrank for Infosys Hackathon
_________________________________________________________________________________________________
        This program prints the index of a sentence in an array of sentences IF
        all the words in a given array of words derived by splitting by space for each element in an array of queries occur in that sentence.
        If the word(s) don't appear in any sentences print(-1)
        Example:
                sentences : ['bob and alice like to text each other', 'bob does not ski', 'alice likes to ski', 'bob and bob are friends']
                queries: ['bob alice', 'like', 'alice', 'likes', 'bob']
                The program prints:
                sentences[0] sentences[0] 
                sentences[0] 
                sentences[0] sentences[2] 
                sentences[2] 
                sentences[0] sentences[1] sentences[3] sentences[3] 
                Explanation:
                        For The First Query: "bob alice":
                                The Words are "bob" and "alice"
                                They both appear in the first sentence which has index 0, hence explicitly two times the index is printed along with the array/
                        For The Second Query: "like":
                                The word "like" appears in only the sentence with the index 0. That is first sentence.
                                Note: In the 3rd sentence: "alice likes to ski", it is "likes" and not "like".
                        For The Last Query (5th one):
                                The Word "bob" appears:
                                        1) 1 Time in 1st sentence
                                        2) 1 Time in 2nd sentence
                                        3)  2 Times in the last sentence. (Hence the sentence's index is printed twice)
              
              
              __________________________________________________________________________________________________
              
              To Count The Occurences of the word(s) in the sentence, I have used the count_occurrences function, which can be found at: 
              https://github.com/susmitpy/subStringOccurences/blob/master/overlapping_occurences_of_substring_in_a_string.py                          
                           
"""

for query in queries:                           
	words = query.split(" ")        #Getting the words by splitting by space
	len_words = len(words)
	results = []
	for index, sen in enumerate(sens):
		sen_result = []
		for word in words:
			ree = re.search(r'\b{}\b'.format(word), sen)    #Searching for string with boundaries
			if ree:
				times = count_occurrences(sen, word)    #Counting The No. Of Occurences
				if times > 1:
					len_words += times - 1          #Verifying if all the words have appeared won't give wrong results
				for i in range(times):
					sen_result.append(result.format(index)) #Appening the indexes 
			else:
				break                                   #One or more words among the given string does not appear in the sentence

		if len(sen_result) >= len_words:                        #All Words appear in the given sentence
			results.extend(sen_result)                      
		else:
			continue                                         #One or more words among the given string does not appear in the sentence
	if len(results) == 0:
		print(-1)                                                      #The word does not appear in any sentence
	else:
		ans = [print(i, end = " ") for i in results]             #Printing the index separated by space
		print()                                                  # New Line for each Query
                
 #All Suggestions Are Welcomed
