"""________________________________________________________________
-------------------------------------------------------------------
Program:        Text editor
Author:         Tyler Jusczak
Date Modified : 11/06/20
Version :       1.0
Purpose:

    Simple GUI interface text editor in Python
    Type out a document, and save it with buttons.

___________________________________________________________________
-------------------------------------------------------------------"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
import random

class window(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self)
        self.setTitle("Hang Man")
        self.setResizable(True)
        self.setSize(400,600)

        wordPool = ["taffy", "creature", "shout", "camera", "listen",
                "quick", "charge", "viking", "america", "count",
                "rifle", "willow", "rogue", "studio", "storm",
                "window", "chrome", "world", "minnesota", "diamond"]
        self.guessed = []
        self.chosenWord = random.choice(wordPool)
        self.newGuess = ""
        self.lives = 6
        self.endGame = False

        self.gallowPanel = self.addPanel(row = 0, column = 0, columnspan = 1, rowspan = 2)
        self.gallowDraw()

        # Word
        self.wordPanel = self.addPanel(row = 3, column = 0, columnspan = 1)
        # Draw Blanks for init startup
        self.wordDraw()


        # Input
        self.inputPanel = self.addPanel(row = 4, column = 0, columnspan = 1, rowspan = 2, background = "lightgrey")
        self.inputLabel = self.inputPanel.addLabel("Single Letter Guess" , row = 0 , column = 0,  sticky = "N")
        self.inputField = self.inputPanel.addTextField("",row = 1, column = 0, width = 1, sticky ="N")
        self.inputButton = self.inputPanel.addButton("Enter", row = 2, column = 0, command = self.guessController)
        self.inputField.bind("<Return>", lambda event: self.guessController())

        # How to Play
        self.infoPanel = self.addPanel(row = 7, column = 0, columnspan = 1, background = "black")
        self.infoPanel.addLabel("""How to  Play\n\
        - Type a single letter and press enter to guess a letter  -\n\
        -        If you guess incorrectly 6 times, you lose         -\n\
        -                Win by completing the word                   -""", row = 0, column = 0, sticky ="NSEW" , background = "grey")



    def guessController(self):

        # Get the new guess from input field
        self.newGuess = self.inputField.getText()

        # This check if the new guess is valid. If it is only 1 char long and is only letters it is validified.
        valid = False
        if len(self.newGuess) == 1 and self.newGuess.isalpha():
            valid = True

        # If guess is valid, it will be check against the chosen word and previous guessed Letters
        # Depending on the results, the guess can be a new correct guess, new incorrect guess, or already guessed.
        # ONLY NEW INCORRECT GUESSED SUBRACT A LIFE
        if valid == True:
            if self.newGuess in self.chosenWord and self.newGuess not in self.guessed and self.lives > 0:
                print("New Correct Guess")
            elif self.newGuess not in self.chosenWord and self.newGuess not in self.guessed and self.lives > 0:
                print("New IncorrectGuess")
                self.lives -= 1
            else:
                print("Already Guessed")

            # Add new guess to list of guessed letters
            self.guessed.append(self.newGuess)
            self.inputField.setText("")

            # Redraw word line with new guess info
            self.wordDraw()
            # Redraw gallows image
            self.gallowDraw()
        else:
            print("INVALID")
            self.inputField.setText("")

    def wordDraw(self):

        if self.lives > 0:

            # Drawing the Letters & Blanks

            blanks = 0      # For checking to see if the user has won.
            columnCount = 1 # Keeps track of where to draw next letter
            self.wordPanel.addLabel(text = "|||", row = 1 , column = 0, font = 20, sticky = "NSEW")
            for letter in self.chosenWord:
                if letter in self.guessed:
                    # If the letter is already in guessed letters, then display it.
                    self.wordPanel.addLabel(text = letter.upper(), row = 1 , column = columnCount, font = 20, sticky = "NSEW")
                    columnCount += 1

                else:
                    # If the letter is not in guessed letters, then display a blank.
                    self.wordPanel.addLabel(text = "_", row = 1 , column = columnCount, font = 20, sticky = "NSEW")
                    columnCount += 1
                    blanks += 1
            self.wordPanel.addLabel(text = "|||", row = 1 , column = columnCount + 1, font = 20, sticky = "NSEW")

            # After displaying the word, if no blanks were drawn, then the user has won
            if blanks == 0:
                self.endPanel = self.addPanel(row = 4, column = 0, background ="lightgrey")
                self.endPanel.addLabel(text = "! ! You Won ! !", row =1, column =0, font = 25, foreground = "white", background = "darkgreen", sticky ="NSEW")

        if self.lives == 0:
            self.endPanel = self.addPanel(row = 4, column = 0, background ="lightgrey")
            self.endPanel.addLabel(text = "You Lost", row =1, column =0, font = 25, foreground = "white", background = "maroon", sticky ="NSEW")
            self.endPanel.addLabel(text = "The word was : " + str(self.chosenWord), row =2, column =0, font = 25, foreground = "white", background = "maroon", sticky ="NSEW")

    def gallowDraw(self):

        # Set the image lable inside the gallow panel.
        self.imageLabel = self.gallowPanel.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")

        # Depending on the lives remaining, the image will change.
        if self.lives == 6:
            self.gallowImage = PhotoImage(file = "hang1.png")
        elif self.lives == 5:
            self.gallowImage = PhotoImage(file = "hang2.png")
        elif self.lives == 4:
            self.gallowImage = PhotoImage(file = "hang3.png")
        elif self.lives == 3:
            self.gallowImage = PhotoImage(file = "hang4.png")
        elif self.lives == 2:
            self.gallowImage = PhotoImage(file = "hang5.png")
        elif self.lives == 1:
            self.gallowImage = PhotoImage(file = "hang6.png")
        elif self.lives == 0:
            self.gallowImage = PhotoImage(file = "hang7.png")

        # Set the selected image to the imageLable
        self.imageLabel["image"] = self.gallowImage



def main():
    window().mainloop

if __name__ == '__main__':
    main()
