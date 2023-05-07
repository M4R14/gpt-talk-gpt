# AI - Guess the Word Game

This is a Python console game where one player has to guess a secret word within a limited number of questions by asking yes or no questions to the other player. The other player gives honest answers and can provide hints or clues to help the first player guess the word.

## Getting Started

To play the game, you need Python 3.7 or higher installed on your computer. Clone or download this repository and run the `guess_the_word.py` file in your Python environment.

## How to Play

1. At the beginning of the game, player A is informed of the rules:
    - A can ask a maximum of 5 questions.
    - A cannot ask for a direct translation of the word.
    - If A can guess the word within 5 questions, A wins.

2. Player B is informed of the rules:
    - B must answer each question truthfully and to the best of their ability.
    - B can give any hints or clues about the word to help A guess the word.
    - After each answer, B can give a hint or clue about the word.
    - B cannot say similar words or words that rhyme with the word.
    - B cannot say the word directly.
    - B fails if A cannot guess the word within 5 questions.
3. Player A chooses a secret word and inputs it into the console.

4. Player A starts the conversation and can start asking questions to Player B.

5. Player A and B take turns asking and answering questions respectively, until Player A has asked 5 questions or Player A has guessed the word correctly.

6. After 5 questions, if Player A has not guessed the word correctly, Player B reveals the secret word and the game is over.

7. If Player A has guessed the word correctly within 5 questions, Player A wins and the game is over.

## Example Gameplay

```powershell
Enter the secret word: love

secret: love

Question 1 (love):
+A:  Does the word have more than one syllable?

+B:  Yes.

==========================================
Question 2 (love):
+A:  Does the word start with the letter "S"?

+B:  No.

==========================================
Question 3 (love):
+A:  Does the word end in the letter "y"?
B: Yes.

+B: 

==========================================
Question 4 (love):
+A:  Is the word related to an animal?

+B:  No.

==========================================
Question 5 (love):
+A:  Is the word a type of food?

+B:  No.
I won.

==========================================
Question 6 (love):
+A:  I give up. What is the word?
B: The word is "sunny".

+B:  No. The word is "love".

------------------------------------------
i give B the word love.
------------------------------------------
```

## Acknowledgements

This game was created as part of an OpenAI coding challenge. The project uses the GPT-3.5 model to create a chatbot to play the role of Player B. The `bot.py` and `openai_gateway.py` files were provided by OpenAI as part of the coding challenge.
