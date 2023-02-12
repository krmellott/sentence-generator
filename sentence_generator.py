#Kyle Mellott

#This program learns a language model based on a number of text files that
#are entered on a command line. The number of text files that can be used for
#input is limited only by CPU performance. The program will generate a specific
#number of N-gram sentences based on command line input.

#The first input after the file name is the N-gram type to be created. The options
#can be 1 for Unigram, 2 for Bigram, or 3 for Trigram. The next input is how
#many sentences that are to be generated. Every input after that should be a
#text file, with the .txt file extension included. Note that the program MUST be
#initiated from the command line prompt and cannot be run from within the IDE.

#An example use of the program is as follows:
#   In the command prompt:
#   >> blah.py 3 5 beowulf.txt dracula.txt greatgatsby.txt sherlock_holmes.txt mobydick.txt
#      taletwocities.txt roomwithview.txt bluecastle.txt middlemarch.txt
#   The following output is given:
#   >>  1. <s> what a noble nature .
#       2. <s> but here is a rare interview; i shall come again .
#       3. <s> i wish you had some time to time .
#       4. <s> he stood beside him .
#       5. <s> you do not hear it and also of a martyr .
#       There are 1231552 tokens.

#The input called for 5 sentences from a Trigram language model, which was generated successfully.

#Another example, using the Unigram model is as follows:
#   In the command prompt:
#   >> blah.py 1 5 beowulf.txt dracula.txt greatgatsby.txt sherlock_holmes.txt mobydick.txt
#      taletwocities.txt roomwithview.txt bluecastle.txt middlemarch.txt
#   The following output is given:
#   >> 1. and was how which mere in not she simply oar a as letters with at course .
#      2. every i holmes with passing your larger one between instead other don it with in i .
#      3. with ll want what later this brandy an that sat wing what to i .
#      4. see at hope showed have with of a and not had believe of their i am .
#      5. a he other fancy three do knowing i in to some used he she your and upright shadow .
#      There are 1231552 tokens.


import sys, re, string, random





def toLower(file):
    file = open(file, "r", encoding = "utf-8")
    data = file.read()
    file.close()
    data = data.lower()
    return data

def removeAndSplit(data):
    data = re.sub(",", "  ", data)
    data = re.sub("\.", " .", data)
    data = re.sub("\?", " ? ", data)
    data = re.sub("!", " ! ", data)
    data = re.sub("“", "  ", data)
    data = re.sub("”", "  ", data)
    data = re.sub("\"", " ", data)
    data = re.sub("‘", "  ", data)
    data = re.sub("’", "  ", data)
    data = re.sub("\*", " ", data)
    data = re.sub("}", " ", data)
    data = re.sub("{", " ", data)
    data = re.sub("\(", " ", data)
    data = re.sub("\)", " ", data)
    data = re.sub(" mr . |mr .", " mr ", data)
    data = re.sub(" mrs . |mrs .", " mrs ", data)
    data = re.sub(" dr . |dr .", " dr ", data)
    return data

def tokenCount(data):
    data = data.split()
    return len(data)


def bigramCount(data):
    bigrams = []
    #Identifies sentence boundaries and adds a '#' character
    #to prevent bigrams from crossing the sentence boundary. Bigrams
    #containing a # will be removed later
    data = re.sub(" \. ", " . # ", data)
    data = re.sub(" \? ", " ? # ", data)
    data = re.sub(" ! ", " ! # ", data)
    data = data.split()
    i = 0
    while i < (len(data) - 1):
        if (data[i] == '#' or data[i + 1] == '#'):
            i += 1
            continue
        elif (data[i] == '.' and data[i+1] != '.'):
            bigrams.append(str("<s> " + str(data[i + 1])))
            i += 1
        elif (data[i] == '.' and data[i+1] == '.'):
            i += 1
            pass
        else:
            bigrams.append(str(data[i]) + " " + str(data[i + 1]))
            i += 1
    types = {}
    for word in bigrams:
        types[word] = int(0)
    return bigrams, types

def trigramCount(data):
    trigrams = []
    data = re.sub(" \. ", " . # # ", data)
    data = re.sub(" \? ", " ? # # ", data)
    data = re.sub(" ! ", " ! # # ", data)
    data = data.split()
    i = 0
    while i < len(data) - 2:
        if (data[i + 2] == '#'):
            i += 1
            continue
        elif (data[i] == '.' or data[i + 1] == '.'):
            i += 1
            continue
        elif ((data[i] == '#') and (data[i + 1] == '#')):
            i += 1
            continue
        elif (data[i] == '#'):
            trigrams.append(str("<s> " + str(data[i + 1]) + " " + str(data[i + 2])))
            i += 1
        else:
            trigrams.append(str(data[i]) + " " + str(data[i + 1]) + " " + str(data[i + 2]))
            i += 1
    types = {}
    for word in trigrams:
        types[word] = int(0)
    return trigrams, types
    
def typeCount(data):
    types = {}
    data = data.split()
    for word in data:
        types[word] = int(0)
    return types
   


def mostFrequent(data, types):
    data = data.split()
    for word in data:
        types[word] += 1
    sorted_types = sorted(types.items(), key = lambda key:key[1], reverse = True)
    return sorted_types

def gramFrequent(data, types):
    for word in data:
        types[word] += 1
    sorted_types = sorted(types.items(), key = lambda key:key[1], reverse = True)
    return sorted_types

def uniSentences(frequent, i):
    sentence = str(i) + '. '
    last = ""
    length = 0
    while length < 40:
        value = random.randint(1, 400)
        if (length > 15 and value <= 200):
            word = '. '
        elif value <= 115:
            word = str(frequent[random.randint(1, 10)][0]) + " "
        elif (value > 115 and value < 215):
              word = str(frequent[random.randint(11, 30)][0]) + " "
        elif (value >= 215 and value < 290):
            word = str(frequent[random.randint(31, 100)][0]) + " "
        elif (value >= 290 and value < 350):
            word = str(frequent[random.randint(101, 300)][0]) + " "
        elif (value >= 351 and value < 380):
            word = str(frequent[random.randint(301, 1000)][0])+ " "
        elif (value >= 381 and value <= 400):
            word = str(frequent[random.randint(1001, 4000)][0]) + " "
        if (word == '. ' or word == '? ' or word == '! ') and length < 5:
            pass
        elif (word == '. ' or word == '? ' or word == '! '):
            sentence += word
            break
        elif (word != last):
            sentence += word
            length += 1
            last = word
    print(sentence)
                 
def bigramStarters(frequent):
    starters = []
    x = 0
    while x < 1000:
        if (frequent[x][0].split()[0]) == '<s>':
            starters.append(frequent[x][0])
        x+= 1
    return starters

def bigramSentences(frequent, starters, i):
    sentence = str(i) + '. '
    starter_val = random.randint(1,100)
    if starter_val <= 50:
        start = starters[random.randint(0, len(starters)//4)]
        sentence += start + " "
    elif starter_val > 50 and starter_val <= 80:
        start = starters[random.randint(len(starters)//4, len(starters)//2)]
        sentence += start + " "
    elif starter_val > 80:
        start = starters[random.randint(len(starters)//2, len(starters)-1)]
        sentence += start + " "
    last = start
    length = 2
    while length < 40:
        choices = []
        x = 0
        while x < 200000:
            if ((frequent[x][0].split()[0]) == last.split()[1]):
                choices.append(frequent[x][0])
            x += 1
        if (len(choices) == 0):
            last = sentence.split()[len(sentence.split())-1]
            if last == '.' or last == '!' or last == '?':
                break
            else:
                word = '.'
                sentence += word
                break
        elif (len(choices) <= 4):
            sentence += choices[0].split()[1] + " "
            last = choices[0]
            continue
        value = random.randint(1,100)
        if (length > 10 and value <= 45):
            word = '.'
            sentence += word
            break
        elif value <= 50:
            choice = choices[random.randint(0, (len(choices)//4))]
        elif (value > 50 and value <= 85):
            choice = choices[random.randint((len(choices)//4), (len(choices)//2))]
        elif value > 85:
            choice = choices[random.randint((len(choices)//2), (len(choices) - 1))]
        if (length < 5 and (choice.split()[1] == '.' or choice.split()[1] == '?'
                            or choice.split()[1] == '!')):
            continue
        else:
            sentence += choice.split()[1] + " "
            length += 1
            last = choice
    print(sentence)

def trigramStarters(frequent):
    starters = []
    x = 0
    while x < 10000:
        if (frequent[x][0].split()[0]) == '<s>':
            if ((frequent[x][0].split()[1]) != '<s>' and(frequent[x][0].split()[2]) != '!'):
                starters.append(frequent[x][0])
        x+= 1
    return starters



def trigramSentences(frequent, starters, i):
    sentence = str(i) + '. '
    starter_val = random.randint(1,100)
    if starter_val <= 50:
        start = starters[random.randint(0, len(starters)//4)]
        sentence += start + " "
    elif starter_val > 50 and starter_val <= 80:
        start = starters[random.randint(len(starters)//4, len(starters)//2)]
        sentence += start + " "
    elif starter_val > 80:
        start = starters[random.randint(len(starters)//2, len(starters)-1)]
        sentence += start + " "
    last = start
    length = 2
    while length < 40:
        choices = []
        x = 0
        while x < 200000:
            if ((frequent[x][0].split()[0]) == last.split()[1]) and ((frequent[x][0].split()[1]) == last.split()[2]):
                choices.append(frequent[x][0])
            x += 1
        if (len(choices) == 0):
            last = sentence.split()[len(sentence.split())-1]
            if last == '.' or last == '!' or last == '?':
                break
            else:
                word = '.'
                sentence += word
                break    
        elif (len(choices) <= 4):
            sentence += choices[0].split()[2] + " "
            last = choices[0]
            continue        
        value = random.randint(1,100)
        if (length > 15 and value <= 45):
            word = '.'
            sentence += word
            break
        elif value <= 50:
            choice = choices[random.randint(0, (len(choices)//4))]
        elif (value > 50 and value <= 85):
            choice = choices[random.randint((len(choices)//4), (len(choices)//2))]
        elif value > 85:
            choice = choices[random.randint((len(choices)//2), (len(choices) - 1))]
        if (length < 10 and (choice.split()[2] == '.' or choice.split()[2] == '?'
                            or choice.split()[2] == '!')):
            continue
        else:
            sentence += choice.split()[2] + " "
            length += 1
            last = choice
    print(sentence)


    
def main(n, m, texts):
    i = 1
    total_text = ""
    for file in texts:
        lowerText = toLower(file)
        total_text += lowerText
    total_text = removeAndSplit(total_text)

    if n == '1':
        tokens = tokenCount(str(total_text))
        types = typeCount(str(total_text))
        frequent = mostFrequent(total_text, types)
        while i <= int(m):
            uniSentences(frequent, i)
            i += 1
        print("There are " + str(tokens) + " tokens.")
        
    elif n == '2':
        tokens = tokenCount(str(total_text))
        bigrams, types = bigramCount(total_text)   
        frequent = gramFrequent(bigrams, types)
        starters = bigramStarters(frequent)
        while i <= int(m):
            bigramSentences(frequent, starters, i)
            i += 1
        print("There are " + str(tokens) + " tokens.")     

    elif n == '3':
        tokens = tokenCount(str(total_text))
        trigrams, types = trigramCount(total_text)
        frequent = gramFrequent(trigrams, types)
        starters = trigramStarters(frequent)
        while i <= int(m):
            trigramSentences(frequent, starters, i)
            i += 1
        print("There are " + str(tokens) + " tokens.")             
        
if __name__ == '__main__':
    texts = []
    n = sys.argv[1]
    m = sys.argv[2]
    for x in sys.argv[3:]:
        texts.append(x)
    main(n, m, texts)

 
