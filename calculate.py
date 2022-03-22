import json, csv, math

# Defines an alphabet, and makes it "loopable"
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphabet = alphabet + alphabet

def calculateClicks(pChar, cChar):

    distances = []

    try:

        # Uses four indexes to check if looping around is more efficient than backtracking
        # The lowest offset is returned

        pIndex1 = alphabet.index(pChar.upper())
        cIndex1 = alphabet.index(cChar.upper())
        pIndex2 = alphabet.index(pChar.upper(), math.floor(len(alphabet) / 2))
        cIndex2 = alphabet.index(cChar.upper(), math.floor(len(alphabet) / 2))

        distances.append(math.dist((pIndex1,), (cIndex1,)))
        distances.append(math.dist((pIndex1,), (cIndex2,)))
        distances.append(math.dist((pIndex2,), (cIndex1,)))
        distances.append(math.dist((pIndex2,), (cIndex2,)))

        return min(distances)

    except Exception as e:
        print(e)

def loopEachWord(dict):

    print("[+] Calculating clicks for each word in dictionary...")
    totalClicksResults = {}

    for word in dict:
        totalClicks = 0
        clicks = 0
        previousChar = ""

        for char in word:
            if not previousChar:
                clicks = calculateClicks("A", char) # A is the default starting point
                previousChar = char
            else:
                clicks = calculateClicks(previousChar, char)

            totalClicks += clicks

        totalClicksResults[word] = int(totalClicks + len(word))

    print("[+] Finished calculating")
    return totalClicksResults

def loadDict(dictFile):

    print("[+] Reading", dictFile)

    dict = open(dictFile).read().split()

    print("[+] Loaded dictionary has", len(dict), "words")
    return dict

def writeCSVFile(fileName, dict):

    print("[+] Writing results to", fileName)

    with open(fileName, 'w') as f:
        f.write("%s, %s\n" % ('Word', 'Clicks needed'))

        for word in dict.keys():
            f.write("%s, %s\n" % (word, dict[word]))

        print("[+] Finished writing to", fileName)

def main():

    dict = loadDict("dictionary.txt")

    totalClicksResults = loopEachWord(dict)

    print("[+] Worst possible word to enter, with clicks needed:", sorted(totalClicksResults.items(), key=lambda x: x[1], reverse=True)[0])

    writeCSVFile('TotalClicksNeeded.csv', totalClicksResults)

if __name__ == '__main__':

    main()
