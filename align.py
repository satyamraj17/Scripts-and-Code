def align(array, letter):
    pos = list()
    for word in array:
        pos.append(word.find(letter))
    max_index = max(pos)
    for word, ind in zip(array, pos):
        if ind == -1:
            continue
        print(" "*(max_index-ind)+word)

arr = ['apple','orange','pear','pineapple','durian']
letter = 'a'
align(arr, letter)

"""
Align the list in the below format, matching the first occurrence of the letter. If the letter doesn't exists in a string, it will not be printed.
    apple
  orange
  pear
pineapple
durian
"""
