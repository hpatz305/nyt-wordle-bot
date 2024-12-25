import random

class WordleBot:
    def __init__(self):
        self.word_list = self.load_word_list()
        self.target_word = random.choice(self.word_list)

    def load_word_list(self):
        # Load a list of valid five-letter words from a file named 'words.txt'
        try:
            with open('words.txt') as file:
                return [word.strip().lower() for word in file.readlines()]
        except FileNotFoundError:
            print("Error: 'words.txt' file not found. Please add a valid list of five-letter words.")
            return []

    def make_guess(self, guess, target_word):
        feedback = []
        for i in range(len(guess)):
            if guess[i] == target_word[i]:
                feedback.append('G')  # Correct letter in the correct place
            elif guess[i] in target_word:
                feedback.append('Y')  # Correct letter in the wrong place
            else:
                feedback.append('B')  # Incorrect letter
        return feedback

    def play(self):
        if not self.word_list:
            return
        attempts = 6
        for _ in range(attempts):
            guess = input("Enter your guess: ").strip().lower()
            if len(guess) != 5 or guess not in self.word_list:
                print("Invalid guess. Please enter a valid five-letter word.")
                continue
            feedback = self.make_guess(guess, self.target_word)
            print("Feedback:", ''.join(feedback))
            if guess == self.target_word:
                print("Congratulations! You've guessed the word!")
                return
        print(f"Sorry, the correct word was {self.target_word}.")

if __name__ == "__main__":
    bot = WordleBot()
    bot.play()
