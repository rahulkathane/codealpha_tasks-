"""
╔══════════════════════════════════════════════════════════════╗
║           BASIC RULE-BASED CHATBOT — CodeAlpha Task 4        ║
║  Responds to common phrases using if-elif logic              ║
║  Key concepts: if-elif, functions, loops, input/output       ║
╚══════════════════════════════════════════════════════════════╝
"""

BOT_NAME = "Nova"


# ── Response logic ────────────────────────────────────────────────────────────

def get_response(user_input: str) -> str:
    """
    Match the user's message to a predefined reply.
    Returns the bot's response string, or a fallback message.
    """
    msg = user_input.lower().strip()

    # ── Greetings ──────────────────────────────────────────────
    if msg in ("hello", "hi", "hey", "howdy", "hiya", "sup"):
        return "Hi there! 👋 Great to see you. How can I help?"

    elif msg in ("hello there", "hey there", "hi there"):
        return "Hello! 😊 What's on your mind?"

    elif msg in ("good morning", "morning"):
        return "Good morning! ☀️ Hope you have a wonderful day ahead!"

    elif msg in ("good afternoon", "afternoon"):
        return "Good afternoon! 🌤️ Hope your day is going well!"

    elif msg in ("good evening", "evening"):
        return "Good evening! 🌙 How was your day?"

    # ── How are you ────────────────────────────────────────────
    elif msg in ("how are you", "how are you?", "how r u", "how do you do",
                 "how's it going", "how's it going?", "you good?", "you okay?"):
        return "I'm doing great, thank you for asking! 😊 How about you?"

    elif msg in ("i am fine", "i'm fine", "i am good", "i'm good",
                 "doing well", "i'm okay", "all good"):
        return "Glad to hear that! 😄 Is there anything I can help you with?"

    elif msg in ("not good", "not great", "i'm sad", "i am sad",
                 "feeling bad", "not okay", "i'm not okay"):
        return "I'm sorry to hear that. 😢 I hope things get better soon! I'm here if you want to talk."

    # ── What are you ───────────────────────────────────────────
    elif msg in ("what are you", "who are you", "what are you?", "who are you?"):
        return f"I'm {BOT_NAME}, a simple rule-based chatbot 🤖 built with Python!"

    elif msg in ("what is your name", "what's your name", "your name?", "name?"):
        return f"My name is {BOT_NAME}! Nice to meet you. 😊"

    elif "your name" in msg:
        return f"My name is {BOT_NAME}! 😊"

    elif msg in ("what can you do", "what can you do?", "help", "help me",
                 "commands", "options"):
        return (
            "I can chat about:\n"
            "  • Greetings        — hello, hi, good morning ...\n"
            "  • How are you      — how's it going, you good? ...\n"
            "  • About me         — who are you, what's your name? ...\n"
            "  • Fun stuff        — tell me a joke, fun fact ...\n"
            "  • Time & date      — what time is it, what's today? ...\n"
            "  • Farewells        — bye, goodbye, see you ...\n"
            "  Try any of these! 🙂"
        )

    # ── Jokes ──────────────────────────────────────────────────
    elif msg in ("tell me a joke", "joke", "say something funny",
                 "make me laugh", "funny"):
        return (
            "😄 Why do programmers prefer dark mode?\n"
            "   Because light attracts bugs! 🐛"
        )

    elif msg in ("another joke", "one more joke", "more jokes"):
        return (
            "😂 Why did the Python programmer get kicked out of school?\n"
            "   Because he kept breaking the class!"
        )

    # ── Fun facts ──────────────────────────────────────────────
    elif msg in ("fun fact", "tell me a fact", "fact", "something interesting"):
        return (
            "🤓 Fun fact: Python was named after the comedy group\n"
            "   'Monty Python', not the snake! 🐍"
        )

    # ── Time & date ────────────────────────────────────────────
    elif msg in ("what time is it", "what's the time", "time?", "current time"):
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"🕐 The current time is {now}."

    elif msg in ("what's today", "what day is it", "today's date", "date?",
                 "what is today", "what is the date"):
        from datetime import datetime
        today = datetime.now().strftime("%A, %d %B %Y")
        return f"📅 Today is {today}."

    # ── Thanks ─────────────────────────────────────────────────
    elif msg in ("thank you", "thanks", "thank you!", "thanks!",
                 "ty", "thx", "many thanks"):
        return "You're welcome! 😊 Happy to help anytime."

    elif msg in ("thank you so much", "thanks a lot", "thanks a ton"):
        return "Anytime! 🌟 That's what I'm here for."

    # ── Compliments ────────────────────────────────────────────
    elif msg in ("you're great", "you are great", "you're awesome",
                 "you are awesome", "good bot", "nice bot"):
        return "Aww, thank you! 🥰 You made my circuits happy!"

    elif msg in ("i love you", "i like you"):
        return "That's so sweet! ❤️ I like chatting with you too!"

    # ── Farewells ──────────────────────────────────────────────
    elif msg in ("bye", "goodbye", "good bye", "see you", "see ya",
                 "later", "take care", "cya", "farewell", "quit", "exit"):
        return f"Goodbye! 👋 It was nice talking to you. Have a great day!"

    elif msg in ("bye bye", "byee", "byeee"):
        return "Bye bye! 🌟 Come back anytime!"

    # ── Empty input ────────────────────────────────────────────
    elif msg == "":
        return "Hmm, you didn't type anything. Try saying 'hello'! 😊"

    # ── Fallback ───────────────────────────────────────────────
    else:
        return (
            f"I'm not sure how to respond to '{user_input}'. 🤔\n"
            "  Try: hello / how are you / tell me a joke / bye\n"
            "  Or type 'help' to see what I can do!"
        )


def is_farewell(msg: str) -> bool:
    """Returns True if the user wants to end the conversation."""
    farewells = {"bye", "goodbye", "good bye", "see you", "see ya",
                 "later", "cya", "exit", "quit", "farewell", "bye bye"}
    return msg.lower().strip() in farewells


# ── Main chat loop ────────────────────────────────────────────────────────────

def chat():
    """Start and run the chatbot conversation loop."""
    print("\n" + "═" * 55)
    print(f"   Welcome to {BOT_NAME} — Your Python Chatbot 🤖")
    print("   Type 'help' to see topics  |  'bye' to exit")
    print("═" * 55 + "\n")

    print(f"  {BOT_NAME} : Hello! I'm {BOT_NAME}. What would you like to talk about?\n")

    while True:
        # Get user input
        user_input = input("  You   : ").strip()

        # Get and print bot response
        response = get_response(user_input)
        print(f"\n  {BOT_NAME}  : {response}\n")

        # End conversation on farewell
        if is_farewell(user_input):
            break


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    chat()
