import json
import difflib
data=json.load(open("data.json","r"))
word=input("Enter a word: ")
def my_dict(word):
    if word in data:
        return data[word]
    else:
        word=word.lower()
        if word in data:
            return data[word]
        elif difflib.get_close_matches(word,data.keys())[0] in data:
            yes_no=input("Do u mean..??? %s \n If Yes print 'Y' else 'N' :" %(difflib.get_close_matches(word,data.keys())[0]))
            if yes_no=='Y':
               return data[difflib.get_close_matches(word,data.keys())[0]]
            elif yes_no=='N':
               print("There is no similar word in my dictionary...Please double check it..!!!")
               further=input("Would you like to continue the search?\nIf 'yes' enter 'Y' else 'N': ")
               if further=='Y':
                   w=input("Enter a word:")
                   return my_dict(w)
               else:
                   return "Thanks for the usage...Happiiee Day...!!!"
            else:
                return "Your entry doesn't existss..."
        else:
            return "Your entry doesn't existss..."



output=my_dict(word)
if type(output)==list:
    for item in output:
        print(item)
elif type(output)==str:
    print(output)
