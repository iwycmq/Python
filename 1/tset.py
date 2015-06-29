input_sentence=raw_input("input a sentence: ")
words=input_sentence.split(" ")
result=""
for word in words:
    if word=="red":
        result+="***"
    elif word=="yellow":
        result+="******"
    elif word=="blue":
        result+="****"
    elif word=="green":
        result+="*****"
    else:
        result+=word
    result+=" "
result=result[0:len(result)-1]
print result
