sentence = "way a is there will is there Where"

def reverse_sentence(sentence:str) -> str:
    reversed_sentence = list()
    sentence = sentence.split(" ")
    for i in range(-1,-(len(sentence))-1, -1):
        reversed_sentence.append(sentence[i])
    reversed_sentence = (" ").join(reversed_sentence)
    return reversed_sentence

print(reverse_sentence(sentence))