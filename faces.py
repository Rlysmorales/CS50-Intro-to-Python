def main():
    user_input = input()
    convert(user_input)


def convert(user_input):
    user_input = user_input.replace(":)", "🙂")
    answer = user_input.replace(":(", "🙁")
    print(answer)
    return answer

main()