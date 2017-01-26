
import string

def word_frequency(file_name):
    frequency = dict()
    file_ref = open(file_name)

    while(True):
        line = file_ref.readline()
        if(len(line) <= 0):
            break
        
        words = line.split(" ")

        for word in words:
            print(word)
            word = word.strip(string.whitespace + string.punctuation)
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency



frequency_map = word_frequency("file.txt")
print(frequency_map)


        