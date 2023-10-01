# #Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkanswer(self, answer):
        return self.answer == answer

  

# q1 = Question('Which is the best software language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')
# q2 = Question('Which is the most popular  software language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')
# q3 = Question('Which is the most pays software language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')

# # print(q1.checkanswer('Python'))
# # print(q2.checkanswer('Java'))
# # print(q3.checkanswer('Python'))




#Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0 
        self.questionIndex = 0


    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('Answer: ')
        self.guess(answer)
        self.loadQuestions()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkanswer(answer):
            self.score += 1
        
        self.questionIndex += 1

    
    def loadQuestions(self):
        if len(self.questions) == self.questionIndex:
            self.showscore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showscore(self):
        print(f'Score: {self.score}')

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz finished...')

        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('Which is the best programming language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')
q2 = Question('Which is the most popular programming language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')
q3 = Question('Which is the most pays programming language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')
q4= Question('Which is the most funniest programming language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')
q5 = Question('Which is the most easiest programming language?', ['C#', 'Python', 'Javasicrpt', 'Java'], 'Python')
questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)
quiz.loadQuestions()
