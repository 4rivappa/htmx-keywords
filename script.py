
def get_words(input_file):
    words = set()
    with open(input_file, 'r') as f:
        for line in f:
            if line.strip() != "":
                words.add(line.strip())
    words = list(words)
    words.sort()
    for word in words:
        print(word)
    print(len(words))
    # write words to a file
    with open('words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')

if __name__ == '__main__':
    get_words('keywords.txt')