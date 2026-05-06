import sys
sys.stdout.reconfigure(encoding='utf-8')
import time

questions = [
    ("At social events, you usually:", "A) Talk to many people", "B) Stay with a few close people", "E", "I"),
    ("You trust more:", "A) Facts", "B) Ideas", "S", "N"),
    ("You decide using:", "A) Logic", "B) Emotions", "T", "F"),
    ("Your style is:", "A) Planned", "B) Flexible", "J", "P"),
    ("Weekend preference:", "A) Go out", "B) Stay home", "E", "I"),
    ("You notice:", "A) Details", "B) Patterns", "S", "N"),
    ("Others see you as:", "A) Firm", "B) Warm", "T", "F"),
    ("You prefer:", "A) Schedule", "B) Spontaneity", "J", "P"),
    ("Energy comes from:", "A) People", "B) Alone time", "E", "I"),
    ("More interesting:", "A) Real things", "B) Possibilities", "S", "N"),
    ("You value:", "A) Fairness", "B) Compassion", "T", "F"),
    ("Work style:", "A) Organized", "B) Adaptable", "J", "P"),
    ("You usually:", "A) Speak first", "B) Think first", "E", "I"),
    ("You focus on:", "A) Present", "B) Future", "S", "N"),
    ("Conflict solution:", "A) Truth", "B) Harmony", "T", "F"),
    ("Trips should be:", "A) Planned", "B) Open-ended", "J", "P"),
    ("Meeting new people feels:", "A) Exciting", "B) Tiring", "E", "I"),
    ("You learn by:", "A) Experience", "B) Imagination", "S", "N"),
    ("Hard choice? Use:", "A) Head", "B) Heart", "T", "F"),
    ("Deadlines:", "A) Finish early", "B) Last minute", "J", "P"),
    ("You are more:", "A) Outgoing", "B) Reserved", "E", "I"),
    ("You trust:", "A) What is proven", "B) Instinct", "S", "N"),
    ("Feedback style:", "A) Honest", "B) Gentle", "T", "F"),
    ("Life preference:", "A) Structure", "B) Freedom", "J", "P"),
    ("Ideal evening:", "A) Group hangout", "B) Quiet reflection", "E", "I"),
]

descriptions = {
    "INTJ": "The Mastermind - Strategic, independent, visionary.",
    "INTP": "The Thinker - Curious, analytical, innovative.",
    "ENTJ": "The Commander - Bold, efficient, natural leader.",
    "ENTP": "The Debater - Creative, energetic, loves ideas.",
    "INFJ": "The Advocate - Insightful, caring, purposeful.",
    "INFP": "The Mediator - Idealistic, loyal, imaginative.",
    "ENFJ": "The Protagonist - Inspiring, empathetic, social.",
    "ENFP": "The Campaigner - Enthusiastic, spontaneous, warm.",
    "ISTJ": "The Inspector - Reliable, practical, disciplined.",
    "ISFJ": "The Protector - Supportive, patient, thoughtful.",
    "ESTJ": "The Executive - Organized, direct, dependable.",
    "ESFJ": "The Consul - Friendly, caring, responsible.",
    "ISTP": "The Virtuoso - Calm, hands-on, adaptable.",
    "ISFP": "The Adventurer - Gentle, artistic, flexible.",
    "ESTP": "The Entrepreneur - Energetic, bold, action-driven.",
    "ESFP": "The Entertainer - Fun, lively, people-loving."
}

# NEW: Abbreviation meanings
meaning = {
    "I": "Introvert",
    "E": "Extrovert",
    "S": "Sensing",
    "N": "Intuition",
    "T": "Thinking",
    "F": "Feeling",
    "J": "Judging",
    "P": "Perceiving"
}

scores = {"I":0,"E":0,"S":0,"N":0,"T":0,"F":0,"J":0,"P":0}

print("="*50)
print("🔥 WELCOME TO PERSONALITY TYPE ANALYZER")
print("="*50)
print("Answer 25 questions honestly using A or B.\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}. {q[0]}")
    print(q[1])
    print(q[2])

    while True:
        ans = input("Your answer (A/B): ").upper()
        if ans == "A":
            scores[q[3]] += 1
            break
        elif ans == "B":
            scores[q[4]] += 1
            break
        else:
            print("Please enter A or B.")

    print()

print("🔍 Analyzing your personality...")
time.sleep(2)

result = ""
result += "I" if scores["I"] >= scores["E"] else "E"
result += "S" if scores["S"] >= scores["N"] else "N"
result += "T" if scores["T"] >= scores["F"] else "F"
result += "J" if scores["J"] >= scores["P"] else "P"

# NEW: Expand abbreviations
expanded = " | ".join([f"{char} = {meaning[char]}" for char in result])

print("\n" + "="*50)
print(f"✨ Your Personality Type: {result}")
print(expanded)
print("="*50)
print(descriptions[result])
print("="*50)