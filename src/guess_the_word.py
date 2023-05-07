
from classes.bot import Bot, Memory
from classes.openai_gateway import MockGateway, OpenAIGateway

OPENAI_API_KEY = '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'


def main():
    MAX_QUESTION = 5
    OPENAI_ENGINE = "text-davinci-003"

    # Create gateway
    gateway = OpenAIGateway(
        engine=OPENAI_ENGINE,
        api_key=OPENAI_API_KEY
    )

    mock_gateway = MockGateway()

    # Create bots
    bot_a = Bot("A", mock_gateway, Memory())
    bot_b = Bot("B", mock_gateway, Memory())

    bot_a.listen("staff", "\n".join([
        f"A can ask a maximum of {MAX_QUESTION} questions.",
        # "Each question must be a 'yes' or 'no' question.",
        "A cannot ask for a direct translation of the word.",
        f"if A can guess the word within {MAX_QUESTION} questions, A wins.",
        # "The word is a number.",
    ]))
    bot_b.listen("staff", "\n".join([
        "B must answer each question truthfully and to the best of their ability.",
        "B can give any hints or clues about the word to help A guess the word.",
        "After each answer, B can give a hint or clue about the word.",
        "B cannot say similar words or words that rhyme with the word.",
        "B cannot say the word directly.",
        # "B can give clues to help A guess the word.",
        f"B faile if A cannot guess the word within {MAX_QUESTION} questions.",
    ]))

    # random word
    secret = input("Enter the secret word: ")

    print(f"secret: {secret}\n")

    bot_b.listen("staff", f"The word is {secret}.")

    # bot_a.listen("staff", "You can start asking questions.")

    # Start conversation
    bot_a.listen(bot_b.name, "I have the word in my mind.")

    for i in range(MAX_QUESTION + 1):
        bot_a.listen('staff', f"Question {i+1}:")
        bot_b.listen('staff', f"Question {i+1}:")

        print(f"Question {i+1} ({secret}):")

        a_ask = bot_a.speak()
        bot_b.listen(bot_a.name, a_ask)

        b_answer = bot_b.speak()
        bot_a.listen(bot_b.name, b_answer)

        print(f"+{bot_a.name}: {a_ask}\n")
        print(f"+{bot_b.name}: {b_answer}\n")
        print("==========================================")

    bot_a.listen('staff', 'End of the game.')
    bot_a.listen('staff', 'What is the word?')
    answer = bot_a.speak()
    print(f"What is the word?: {answer}")
    bot_a.listen('staff', f"i give B the word {secret}.")

    print("------------------------------------------")
    print(f"i give B the word {secret}.")
    print("------------------------------------------")


if __name__ == "__main__":
    main()