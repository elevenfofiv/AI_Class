def find_string(inputs:str) -> list:
    temp_inputs = inputs
    for word in inputs:
        if (word.isdigit()) == True:
            temp_inputs = temp_inputs.replace(word, " ")
    string_list = temp_inputs.split()
    return string_list

inputs = "cat32dog16cow5"
string_list = find_string(inputs)

print(string_list)

