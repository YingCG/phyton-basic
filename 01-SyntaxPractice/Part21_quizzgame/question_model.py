from data import question_data 

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
    
    def newQuestion():
        new_question = question_data["text"]
        print(new_question)
        
    def checkAnswer(answer):
        if answer == question_data.answer:
            True
        
