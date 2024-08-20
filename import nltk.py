import nltk
import re
import random
from nltk.chat.util import Chat, reflections

# Predefined responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great!",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, so I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["I was created by a programmer.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I live in the cloud, where everything is digital.']
    ],
    [
        r"how (.*) weather in (.*)?",
        ["Weather in %2 is awesome like always", "Too hot here in %2", "Too cold here in %2", "Never heard about %2"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company, I have heard a lot about it."]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in %2 for the past few days", "It's raining quite heavily in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy.",]
    ],
    [
        r"(.*)(sports|game) ?",
        ["I'm a very big fan of football",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon!"]
    ],
]

# Reflections are a dictionary that changes words like "I am" to "you are"
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create the Chatbot
chatbot = Chat(pairs, reflections)
def chatbot_conversation():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("ChatBot: Bye for now. See you soon!")
            break
        response = chatbot.respond(user_input)
        if response:
            print("ChatBot:", response)
        else:
            print("ChatBot: Sorry, I didn't understand that.")
if __name__ == "__main__":
    chatbot_conversation()
