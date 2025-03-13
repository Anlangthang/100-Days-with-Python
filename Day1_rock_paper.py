import random

# ASCII Art for choices
choices = {
        "kéo": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''',
    "búa": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',

    "bao": '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
}

# List to match choices with indices
options = ["kéo" , "búa" , "bao"]

def get_user_choice():
    """Handles user input and ensures it's a valid choice."""
    while True:
        try:
            user = int(input("Mày chọn gì? 0 là búa, 1 là kéo, 2 là bao: \n").strip())
            if user in [0, 1, 2]:
                return user
            else:
                print("Giá trị không hợp lệ. Vui lòng chọn 0, 1, hoặc 2.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

def play_game():
    """Runs the Rock-Paper-Scissors game."""
    user = get_user_choice()
    computer = random.randint(0, 2)

    # Print user and computer choices
    print(f"\nNgười chơi chọn: {options[user]}")
    print(choices[options[user]])

    print(f"Máy chọn: {options[computer]}")
    print(choices[options[computer]])

    # Determine the winner
    if user == computer:
        print("Hòa!")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("Người chơi thắng!")
    else:
        print("Người chơi thua!")

# Run the game
play_game()
