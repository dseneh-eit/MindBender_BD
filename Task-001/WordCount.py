def count_words(file, num=True) -> dict:
    """
    Returns a dictionary of all unique words and their occurrences.
    file: The path of the text file that contains the list of words
    num: Include numerical text. default is True
    
    Example:
    the: 50
    """

    # import string
    import re

    r = None

    if num:
        r = '[a-zA-Z0-9@\s]+'
    else:
        r = '[a-zA-Z@\s]+'

    dic = {}
    words = []
    with open(file, 'r') as f:
        for line in f:
            line = line.lower()
            line = ''.join(re.findall(r, line))
            words += line.split()

    for w in words:
        dic[w] = dic.get(w, 0) + 1

    return dic


def save_output(dic, filename):
    with open(filename, "a") as f:
        for i in dic.keys():
            f.write(i + ": " + str(dic[i]) + "\n")


def main():
    print('Getting file...')
    f = count_words('Shakespeare.txt')
    print("Reading output...")
    print('Saving output...')
    save_output(f, '../Task-002/output_python.txt')
    print('Done!')


main()
# print(count_words('Shakespeare.txt'))
