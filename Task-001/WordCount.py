def count_words(file, num=True) -> dict:
    """
    Returns a dictionary of all unique words and their occurance.
    file: The path of the text file that contains the list of words
    num: Include numerical text. default is True
    
    Example:
    the: 50
    """
    
    import string
    import re
 
    r = None
    
    if num: r = '[a-zA-Z0-9@\s]+'
    else: r = '[a-zA-Z@\s]+'
        
    
    dic = {}
    words = []
    with open(file,'r') as f:
        for line in f:
            line = line.lower()
            line = ''.join(re.findall(r,line))
            words += line.split()
    
    for w in words:
        dic[w] = dic.get(w, 0) +1
    
    return dic


print(count_words('Shakespeare.txt'))
