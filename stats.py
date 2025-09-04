def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return len(file_contents.split())

def get_num_chars(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    result = dict()
    for letter in file_contents:
        if letter in result:
            result[letter] += 1
        else:
            result.update({letter:1})
    
    return result

def sort_on(items):
    return items["num"]

def sorted_dict(dlist):
    newlist = list()
    for name, value in dlist.items():
        if name.isalpha():
            newlist.append({"char": name,"num": value})
    newlist.sort(reverse=True, key=sort_on)
    return newlist