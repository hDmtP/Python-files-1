from textblob import TextBlob
myLst = ["incorreT", "Spellin"]
corrected_lst=[]
for word in myLst:
    corrected_lst.append(TextBlob(word))
print("Corrected list words are:")
for word in corrected_lst:
    print(word.correct(), end=" ")
