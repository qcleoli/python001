import Tkinter
import random

class Application(Tkinter.Frame):
  def questionSet(self):
    self.q1 = {"How to create a dictionary?": "Created with curly brackets, and have keys and values: one = {\"one\": \"1\"}", "How to create a set?": "Created with curly brackets: one={\"1\", \"2\",\"3\"}", "How to create a tuple?": "Created with round brackets: one=(\"1\",\"2\",\"3\")", "How to create a list?": "Created using square brackets: one=[\"1\",\"2\",\"3\"]"}
    self.questions = self.q1.keys()
    self.testingOne = 0
    r0 = Tkinter.Radiobutton(self)
    self.choiceList = [r0,r0,r0,r0]
    self.currentChoice = Tkinter.StringVar()
    self.nextQuestion()
    self.score = 0
  def createQuestion(self, q):
    question = Tkinter.Label(self)
    question["text"] = q
    question.grid(columnspan=5, row=0, pady=10)
  def nextQuestion(self):
    if self.testingOne < len(self.questions):
      if self.testingOne > 0:
        self.checkAnswer()
      self.createQuestion(self.questions[self.testingOne])
      self.createChoices()
      self.testingOne = self.testingOne + 1
      print(self.testingOne)
  def createChoices(self):
    choiceValues = self.q1.values()
    choices = ['choice', 'choice', 'choice', 'choice']
    answer = random.randrange(0, 4)
    answerValue = self.q1[self.questions[self.testingOne]]
    print(answerValue)
    choices[answer] = answerValue
    for c in range(4):
      if choices[c] == 'choice':
        temporaryChoice = random.randrange(0, len(self.questions))
        while choiceValues[temporaryChoice] in choices:
          temporaryChoice = random.randrange(0, len(self.questions))
        choices[c] = choiceValues[temporaryChoice]
    r = 0
    rownum = 2
#    selectedChoice = Tkinter.StringVar()
    for c in choices:
      self.choiceList[r].grid_forget()
      self.choiceList[r] = Tkinter.Radiobutton(self)
      self.choiceList[r]["text"] = c
      self.choiceList[r]["value"] = c
      self.choiceList[r]["variable"] = self.currentChoice
 #    self.choiceList[r]["command"] = currentChoice
      self.choiceList[r].grid(row=rownum, sticky=Tkinter.W)
      r = r + 1 
      rownum = rownum + 1
  def checkAnswer(self):
    if self.currentChoice.get() == self.q1[self.questions[self.testingOne-1]]:
      self.score = self.score + 1
      print('score is: ', self.score)
  def createWidgets(self):
    self.questionSet()
    QUIT = Tkinter.Button(self)
    QUIT["background"]="#ff0000"
    QUIT["text"] = "QUIT"
    QUIT["command"] = self.quit
    QUIT.grid(row=7, column=0, sticky=Tkinter.W, pady=20)
    next = Tkinter.Button(self)
    next["text"] = "Next Question"
    next["command"] = self.nextQuestion
    next.grid(columnspan=2, row=7, column= 7, pady=20)
  def __init__(self, master=None):
    Tkinter.Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

root = Tkinter.Tk()
app = Application(master=root)
app.master.title('Multiple Choices')
app.mainloop()
root.destroy()