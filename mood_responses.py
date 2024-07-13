# Question 1 Task 1: Your Mood Today
# mood_responses.py
def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "That is great to hear! keep smiling",
        "sad": "I am sorry to hear that. I hope things get better soon.",
        "excited": "Awesome! what is got you so excited?",
        "angry": "Take a deep breath. It is going to be okay.",
        "tired": "make sure to get some rest. you deserve it"
    }
    return responses.get(mood, "I do not recognize that mood, but I hope you have a good day!")
# main.py
import mood_responses
def main():
    mood = input("How are you feeling today?")
    response = mood_responses.mood_response(mood)
    print(response)
if __name__ == "__main__":
    main()

# Question 2 Task 1:Custom Module with Aliases 

