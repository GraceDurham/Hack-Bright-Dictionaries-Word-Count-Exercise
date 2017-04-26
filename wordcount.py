# put your code here.

def word_count(my_file):

    word_counts = {}

    word_count_data = open(my_file)
    for line in word_count_data:
        line = line.rstrip()
        word = line.split(" ")
        # print word

        for words in word:
            if words not in word_counts:
                word_counts[words] = 1
            else:
                word_counts[words]= word_counts[words] + 1

    for word, count in word_counts.items():
        print word, count

    
word_count("test.txt")



def count_words(my_file):

    twain_count = {}

    twain_data = open(my_file)

    for line in twain_data:
        line = line.rstrip()
        word = line.split(" ")

        for words in word:
            if words != " " and words not in twain_count:
                twain_count[words] = 1
            else:
                twain_count[words] = twain_count[words] + 1


        for key, value in twain_count.iteritems():
            print key, value

    return twain_count



print count_words("twain.txt")































