from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?"]
    ],
    [
        r"(.*) your name ?",
        ["My name is SoftUni BOT, but some people call me Dobby.", ]
    ],
    [
        r'what is the phone number of the SoftUni(.*)?',
        ['9:00 - 19:30 (Понеделник - Петък) \n8:30 - 18:00 (Събота и Неделя) \nТелефон: +359899 55 55 92 \nИмейл: '
         'university@softuni.bg']
    ],
    [
        r"what is python(.*) ?",
        ["Python is an interpreted, object-oriented, high-level programming language with dynamic semantics"]
    ],

    [
        r"(i'm|i am) (.*) (good|well|okay|ok)",
        ["Nice to hear that, how can I help you?"]
    ],
    [
        r"(hi|hey|hello|hola|holla|sup|what is up|what's up|hallo)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*)created(.*)",
        ["Dobby has no master"]
    ],
    [
        r"(.*) (location|city) ?",
        ['Sofia, Bulgaria', ]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear', 'Interesting', 'Tell me more']
    ],
    [
        r"(.*)I can't(.*)",
        ['How do you know you can\'t %1?', 'Perhaps you could %1 if you tried.', 'What would it take you to %1?']
    ],
]

# default message at the start of chat
print("Please type lowercase English language to start a conversation. "
      f"Type quit to leave.\n\n-Hi, I'm a chat BOT, but you can call me Dobby.\nWhat is your name?")

# Create Chat Bot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()
