import random

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("Hatali Bilgi")

        if answer == self.answer:
            return True
        else:
            return False

class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("cevap: ")
        if question.checkAnswer(answer):
            self.score += 1
            print("Tebrikler bildiniz.")
        else:
            print("Yanlis cevap.")
        
        self.questionIndex += 1 
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayScore(self):
        print("Test ozetiniz".center(50,'*'))
        puan = 100/len(self.questions)
        toplamPuan = round(self.score * puan)
        print(f"Toplam {len(self.questions)} sorunun {self.score} tanesini bildiniz.")
        print(f"Aldiginiz puan: {toplamPuan}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f"Toplam {totalQuestion} sorunun {questionNumber}. sorusundasiniz.".center(50, '*'))

q1 = Question("En iyi programlama dili hangisidir?",['python', 'dart', 'c#', 'java'], 'python')
q2 = Question("En populer programlama  dili hangisidir?",['c#', 'python', 'dart', 'javascript'], 'python')
q3 = Question("En cok kazandiran programlama dili hangisidir?",['javascript', 'c#', 'dart', 'python'], 'python')

sorular = [q1, q2, q3]

quiz = Quiz(sorular)

print(quiz.displayQuestion())




