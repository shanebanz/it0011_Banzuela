excludedWords = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

def UniqueWordCounter(TextInput):
    WordList = TextInput.split()
    WordTracker = {}

    for Item in WordList:
        ProcessedWord = Item.strip(".,!?;:()")
        if ProcessedWord and ProcessedWord.lower() not in excludedWords:
            WordTracker[ProcessedWord] = WordTracker.get(ProcessedWord, 0) + 1

    LowerWords = sorted([W for W in WordTracker if W.islower()])
    UpperWords = sorted([W for W in WordTracker if W.istitle()])

    TotalFiltered = sum(WordTracker.values())
    
    for W in LowerWords + UpperWords:
        print(W.ljust(10), "-", WordTracker[W])
    
    print("Total words filtered:", TotalFiltered)

InputText = input("Enter a string statement:\n")
UniqueWordCounter(InputText)
