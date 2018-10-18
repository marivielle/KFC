import string
from words import return_words

class parser():

    def __init__(self):
        self.directions = ["go","travel","enter","head"]
        self.actions = ["pick","grab","take","place"]
        self.skip_words = return_words()

    def remove_punct(self,text):

        no_punct = ""
        for char in text:
            if not (char in string.punctuation):
                no_punct += char

        return no_punct


    
    def sentence_to_list(self,sentence):
        return sentence.split()
        
    
    def sense_all(self,string,type_action):
        mainting = False
        list_string = self.sentence_to_list(string)
        print(list_string)
        for i in range(0,len(list_string)-1):
            if list_string[i] in type_action:
                mainting =  True

        return mainting

    def sense_travel(self,string):
        return self.sense_all(string,self.directions)

    def sense_actions(self,string):
        return self.sense_all(string,self.actions)

    
    def calculate_traversal(self,)
            
        
        
        
        
        
