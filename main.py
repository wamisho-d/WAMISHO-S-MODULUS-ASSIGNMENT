import mood_responses
def main():
    mood = input("How are you feeling today?")
    response = mood_responses.mood_response(mood)
    print(response)
if __name__ == "__main__":
    main()