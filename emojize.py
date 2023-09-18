import emoji

def emotions():
    user_input = input("Input: ").strip().lower()
    emoji_result = (emoji.emojize(user_input, language='alias'))
    print("Output:", emoji_result)

emotions()