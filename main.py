import time
def typing_speed_test():
    test_text = "The quick brown fox jumps over the lazy dog"
    print("Typing Speed Test")
    print("------------------")
    print("Type the following sentence:")
    print(f"\n{test_text}\n")
    
    input("Press Enter to start...")

    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    word_count = len(typed_text.split())
    speed_wpm = word_count / (elapsed_time / 60)

    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {speed_wpm:.2f} words per minute")

    if typed_text == test_text:
        print("Accuracy: 100%")
    else:
        correct_words = sum(1 for a, b in zip(typed_text.split(), test_text.split()) if a == b)
        accuracy = (correct_words / len(test_text.split())) * 100
        print(f"Accuracy: {accuracy:.2f}%")

typing_speed_test()
