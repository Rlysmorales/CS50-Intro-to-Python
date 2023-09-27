import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    regex_html = re.search(r'(https?:)[\/\]][\/\]](www\.)?(youtube\.com)[\/\]](embed)[\/\]](.+)"', s)

    if matches := re.search('(".+?")', "http"):
        print(matches.group(1))
        print((regex_html.group(1)))
        print(regex_html[1])

    if regex_html:
        if regex_html[2] is None:
            if regex_html[1] == "http:":
                youtube_modification = regex_html[0].replace("http://youtube.com/embed", "https://youtu.be")
                final_youtube = youtube_modification.rstrip(youtube_modification[-1])
                return final_youtube
            else:
                youtube_modification = regex_html[0].replace("youtube.com/embed", "youtu.be")
                final_youtube = youtube_modification.rstrip(youtube_modification[-1])
                return final_youtube

        elif regex_html:
            if regex_html[1] == "http":
                youtube_modification = regex_html[0].replace("http://www.youtube.com/embed", "https://youtu.be")
                final_youtube = youtube_modification.rstrip(youtube_modification[-1])
                return final_youtube
            else:
                youtube_modification = regex_html[0].replace("www.youtube.com/embed", "youtu.be")
                final_youtube = youtube_modification.rstrip(youtube_modification[-1])
                return final_youtube

    else:
        return None


if __name__ == "__main__":
    main()
