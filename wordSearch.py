# Jack DeGuglielmo & Michael Turner
# 12/6/2020
import os
import codecs
files = []

# Loop through inputs directory
print("Opening file(s): ", end='')
for file in os.listdir('inputs'):
    print(file)
    files.append(os.path.join("C:\\Users\jackd\PycharmProjects\History_Word_Search\inputs", file))


goodbreedCounter = 0
for file in files:
    with codecs.open(file, encoding='utf-8') as f:
    #print(f.read())
        for line in f:
            # print(line)
            # words = line.split()
            # for word in words:
                # print(word)
            if line.__contains__('breeding'):
                print(line)
                goodbreedCounter+=1

    f.close()
print("Number of GB words: ", goodbreedCounter)



