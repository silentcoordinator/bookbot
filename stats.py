def get_word_count(bookString):
    list = bookString.split()
    words = len(list)
    return words

def getCharacterCount(bookString):
    bookString = bookString.lower()
    charDict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
                'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                'm': 0,'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
                's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                'y': 0, 'z': 0}
    for char in bookString:
        if char in charDict:
            charDict[char] += 1
        else:
            continue
    return charDict

def sorting_dict(my_dict):
    # Start with an empty list
    sorted_list = []
    # Iterate over keys and values correctly
    for key, value in my_dict.items():
        temp_dict = {"letter": key, "count": value}
        sorted_list.append(temp_dict)
    # Sort in descending order by 'count'
    sorted_list.sort(reverse=True, key=lambda x: x["count"])

    listwithoutsortingkeys=[]
    for item in sorted_list:
        temp_dict =  {item["letter"] : item["count"]}
        listwithoutsortingkeys.append(temp_dict)

    return listwithoutsortingkeys









