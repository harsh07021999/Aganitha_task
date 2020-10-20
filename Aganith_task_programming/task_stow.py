"""
Author of the library is Harsh Vardhan
from ABVIIITM Gwalior this is interview
prohramming section task by Aganitha Organisation
"""

#These are the general set of rules for the conversion
#These rules could be changed or added in the future
def get_rules():
    rules = {"Numbers":{
                        "zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                        "twenty": 20,
                        "thirty": 30,
                        "forty": 40,
                        "fifty": 50,
                        "sixty": 60,
                        "seventy": 70,
                        "eighty": 80,
                        "ninety": 90,
                        "hundred": 100
                        },
            "Tuples": {
                         "single":1,
                         "double":2,
                         "triple":3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      },
            "General": {
                          "C M": "CM",
                          "P M": "PM",
                          "D M": "DM",
                          "A M": "AM"
                       }
            }
    return rules

#Function to check for the presence of comma or dot at the end and front of the input

def check_front_last(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last


#class that will convert the word
class SpokenToWrittenpy:

    def __init__(self):

        self.rules=get_rules()
        self.paragraph=""
        self.ouptut_para=""

    #user input
    def get_user_input(self):

        self.paragraph=input("\n Enter Your paragraph in english:\n\t")

        if not self.paragraph:
            raise ValueError("You entered nothing.")

    #user output
    def show_output(self):
        print("\nThe input English Paragraph: \n \" "+ self.paragraph+"\"")
        print("\nConverted English Paragraph: \n \"" +self.ouptut_para+"\"")

    
    #main conversion function
    def Translate(self):
        #splitting paragraph into individual words
        words_of_para=self.paragraph.split()
        numbers=self.rules['Numbers']
        tuples=self.rules['Tuples']
        general=self.rules['General']
        i=0
        no_of_words=len(words_of_para)
         
        while i<no_of_words: 
            
            front,word,last=check_front_last(words_of_para[i])
            if i+1!= no_of_words:
            #when word is of the form e.g.: two 
                front_n,next_word,last_n=check_front_last(words_of_para[i+1])
                if word.lower() in numbers.keys() and (next_word.lower()=='dollars' or next_word.lower()=='dollar'):
                    self.ouptut_para=self.ouptut_para+" "+front+"$"+str(numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in tuples.keys() and len(next_word)==1:
                    #when word is of form Triple A
                    self.ouptut_para=self.ouptut_para+" "+front_n+(next_word*tuples[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in general.keys():
                    #if word is of form P M or C M
                    self.ouptut_para=self.ouptut_para+" "+front+word+next_word+last_n
                    i=i+2
                else:
                    self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                    i=i+1
            else:
                self.ouptut_para=self.ouptut_para+" "+words_of_para[i]
                i=i+1


#testing function for the class
obj_spoken=SpokenToWrittenpy()
obj_spoken.get_user_input()
obj_spoken.Translate()
obj_spoken.show_output()

#test()
