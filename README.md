# Smartwatch Click Calculator

Calculates clicks needed to enter a word on a typical smartwatch.

Assumes characters in the order A to Z, with a click needed to step up/down or confirm the selection. Looping from Z to A is possible.

I made this because I god-damn hated entering my Wi-Fi password on my watch, and I'm still mad about it.

# How to use

The script reads *dictionary.json* from the working directory, and calculates the offset between the characters in each word based on a predetermined alphabet.
It uses the offset between each character and the length of the word to determine the amount of clicks needed to enter the word.

The results are written to a .csv file (*TotalClicksNeeded.csv*) in the working directory.
The top scoring entry is additionally written to console together with the clicks needed.

I personally used the .json file from the following github repository: [Websters English Dictionary](https://github.com/matthewreagan/WebstersEnglishDictionary)

Dictionaries from other languages can be used, as long as the *alphabet* variable is updated to contain all the needed characters in their natural order of occurrence.

```sh
git clone https://github.com/Vealending/Smartwatch_Click_Calculator
cd Smartwatch_Click_Calculator
wget https://github.com/matthewreagan/WebstersEnglishDictionary/blob/master/dictionary.json
python3 calculate.py
```

# Conclusion

If you hate your friends, set your Wi-Fi password to "dichlorodiphenyltrichloroethane" (234 clicks) :)
