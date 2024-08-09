import re
import pyperclip
def FindPhoneNumber(text):
    MatchNumber = re.compile(r"""
    (\+\d{1,3})?                            #Country
    [\s.-]?                                 #seprator
    (\(?\d{2,5}\)?)                         #area code execpt contries like india or pakistan it would be also part of main no.
    [\s.-]?                                 #seprator 
    (\d{3,5}[\s\.-]?\d{2,5}[\s\.-]?\d{0,4})
    """,re.VERBOSE)
    
    PhoneNumbers = MatchNumber.findall(text)
    
    res = [ " ".join(tups) for tups in PhoneNumbers]
    for num in res:
        other_char = num.count("-") + num.count(" ") + num.count("(")*2 + num.count("+")
        len_num = len(num) - other_char
        if len_num<10 or len_num>15:
            res.remove(num) 
        
    string_to_paste = "\n".join(res)
    print(string_to_paste)
    return string_to_paste


def Findemail(text):
    Matchemail = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    Match_obj = Matchemail.findall(text)
    string_to_paste = "\n".join(Match_obj)
    print(type(string_to_paste))
    return string_to_paste

text = pyperclip.paste()
emails = Findemail(text)
Phonenumbers = FindPhoneNumber(text)

result  = emails + Phonenumbers
if len(result) > 0:
    print("These Numbers and email are copied to the clipboard")
    print(result)
    pyperclip.copy(result)
else:
    print("No numbers or email has been copied")
    