dict_first = {'사과':30, '배':15, '감':10, '포도':10}
dict_second = {'사과':5, '감':25, '배':15, '귤':25}

def merge_dict(dict_first:dict, dict_second:dict) -> dict:
    keys_first = dict_first.keys()
    keys_second = dict_second.keys()
    merged_keys = sorted(list(set(list(keys_first) + list(keys_second))))
    merged_dict = dict()
    for keys in merged_keys:
        if (keys in keys_first) & (keys in keys_second):
            merged_dict[keys] = dict_first[keys] + dict_second[keys]
        elif (keys in keys_first) & (keys not in keys_second):
            merged_dict[keys] = dict_first[keys]
        elif (keys not in keys_first) & (keys in keys_second):
            merged_dict[keys] = dict_second[keys]
        else:
            pass
    return merged_dict

print(merge_dict(dict_first, dict_second))