from pathlib import Path

dataPath = Path('data')
trainPath = Path(dataPath, 'train.txt')
testPath = Path(dataPath, 'test.txt')
devPath = Path(dataPath, 'dev.txt')
preDevPath = Path(dataPath, 'preDev.txt')
wordsPath = Path(dataPath, 'words.txt')
outPath = Path(dataPath, 'result.txt')


# some common prefix and postfix character
frontCh=['好','可','种','不','大','在','学','小','为','地','的','这','从','新','由','存','对','将','把','被','相']
backCh=['了','到']

# vocabulary with maxWordLen=30
words = []
for i in range(31):
    words.append([])
maxWordLen = 30
with open(wordsPath, encoding='utf-8') as words_f:
    for word in words_f:
        word = word.strip()
        if len(word) > maxWordLen or len(word) < 2:
            continue
        words[len(word)].append(word)
print('total words:', sum([len(it) for it in words])) #84413


def isPunct(ch: str) -> bool:
    return ch in['‘', '“', '”', '，', '。', '？', '！', '：', '；', '、', '《', '》', '『', '』']


def isChinese(ch: str) -> bool:
    if isPunct(ch):
        return False
    return '\u4e00' <= ch <= '\u9fff' or '0' <= ch <= '9'


def seg(line: str) -> str:
    Len = len(line)
    wordList = []
    i = 0

    # find the farthest possible end of a word
    while i < Len:
        j = i
        while j < i+maxWordLen-1:
            if j == Len:
                j -= 1
                break
            # break if line[j] is a punctuation
            if isPunct(line[j]):
                if i != j:
                    j -= 1
                break
            j += 1
        tempWord = line[i:j+1]

        # find the longest matching word in the vocabulary
        while len(tempWord) >= 1:
            if len(tempWord) == 1:
                wordList.append(tempWord)
                break
            # if the word has a common prefix character, recheck it
            # for example, 好学 生 -> 好 学生
            # the new word also cannot end with a common postfix
            if tempWord in words[len(tempWord)]:
                if j+2 < Len and line[i+1:j+2] in words[len(tempWord)] and line[i] in frontCh and line[j+2] not in backCh:
                    wordList.append(line[i])
                    wordList.append(line[i+1:j+2])
                    j += 1
                else:
                    wordList.append(tempWord)
                break
            j -= 1
            tempWord = line[i:j+1]
        i = j+1
    return '  '.join(wordList)

# do the segmentation
out = []
with open(testPath, encoding='utf-8') as test_f:
    for line in test_f:
        line = line.strip()
        line = seg(line)
        out.append(line)
        if len(out) % 100 == 0:
            print(len(out))

# save the result
with open(outPath, 'w', encoding='utf-8') as out_f:
    for line in out:
        out_f.write(line +'\n')