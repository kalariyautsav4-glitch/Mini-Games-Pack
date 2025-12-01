#!/usr/bin/env python3
"""
Mini Games Pack - minigames.py

Games included:
  1) Tic-Tac-Toe (2-player local)
  2) Hangman (vs computer, basic wordlist)
  3) Rock-Paper-Scissors (best of N)
  4) Number Guessing (computer picks, you guess)

How to run:
  python minigames.py

Author: Your Name
For: 1st year B.Tech CSE — feel free to upload to GitHub and expand.
"""

import random
import sys
import time

# ---------------------------
# Tic-Tac-Toe (2-player)
# ---------------------------
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board, mark):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==mark for a,b,c in wins)

def tic_tac_toe():
    board = [str(i+1) for i in range(9)]
    current = "X"
    moves = 0
    print("\nWelcome to Tic-Tac-Toe (2 player).")
    print_board(board)
    while moves < 9:
        try:
            pos = int(input(f"Player {current} - choose cell (1-9): ").strip()) - 1
            if pos < 0 or pos > 8:
                print("Invalid cell. Choose 1-9.")
                continue
            if board[pos] in ("X","O"):
                print("Cell already taken. Try again.")
                continue
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        board[pos] = current
        print_board(board)
        moves += 1
        if check_winner(board, current):
            print(f"🎉 Player {current} wins!\n")
            break
        current = "O" if current == "X" else "X"
    else:
        print("It's a draw!\n")
    input("Press Enter to return to menu...")

# ---------------------------
# Hangman (single-player)
# ---------------------------
HANGMAN_WORDS = [
    "python","computer","program","algorithm","hangman","variable","function",
    "keyboard","internet","development","engineer","network","binary","debug"
]

HANGMAN_PICS = [
    "",
    " O ",
    " O \n | ",
    " O \n/| ",
    " O \n/|\\",
    " O \n/|\\\n/  ",
    " O \n/|\\\n/ \\"
]

def hangman():
    word = random.choice(HANGMAN_WORDS).lower()
    guessed = set()
    tries = 6
    print("\nWelcome to Hangman! Guess the word.")
    while tries > 0 and set(word) != guessed:
        display = " ".join([ch if ch in guessed else "_" for ch in word])
        print("\nWord: ", display)
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "(none)")
        print("Tries left:", tries)
        guess = input("Enter a letter (or full word guess): ").strip().lower()
        if not guess:
            print("Please type a letter or a word.")
            continue
        if len(guess) == 1:
            if guess in guessed:
                print("You already guessed that letter.")
            elif guess in word:
                guessed.add(guess)
                print("Good guess!")
            else:
                tries -= 1
                guessed.add(guess)
                print("Wrong.")
        else:
            # full word guess
            if guess == word:
                guessed.update(word)
                break
            else:
                tries -= 1
                print("Wrong word guess.")
        # show simple hangman art
        print("\nHangman:")
        pic_index = 6 - tries
        print(HANGMAN_PICS[min(pic_index, len(HANGMAN_PICS)-1)])
    if set(word) == guessed:
        print(f"\n🎉 You guessed it! The word was: {word}\n")
    else:
        print(f"\n💀 Out of tries. The word was: {word}\n")
    input("Press Enter to return to menu...")

# ---------------------------
# Rock-Paper-Scissors
# ---------------------------
def rps():
    options = ["rock","paper","scissors"]
    print("\nRock-Paper-Scissors — Best of N")
    try:
        n = int(input("Enter an odd number for 'best of' (e.g. 3,5): ").strip())
        if n <= 0 or n % 2 == 0:
            print("Using default best of 3.")
            n = 3
    except ValueError:
        print("Invalid input, defaulting to 3.")
        n = 3
    needed = n//2 + 1
    score_p = 0
    score_c = 0
    round_no = 1
    while score_p < needed and score_c < needed:
        print(f"\nRound {round_no} — Score You:{score_p} CPU:{score_c}")
        choice = input("Choose rock/paper/scissors (r/p/s): ").strip().lower()
        mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        player = mapping.get(choice, choice if choice in options else None)
        if player is None:
            print("Invalid choice. Try r/p/s or rock/paper/scissors.")
            continue
        comp = random.choice(options)
        print(f"CPU chose: {comp}")
        if player == comp:
            print("It's a tie.")
        elif (player == "rock" and comp == "scissors") or \
             (player == "paper" and comp == "rock") or \
             (player == "scissors" and comp == "paper"):
            print("You win the round!")
            score_p += 1
        else:
            print("CPU wins the round.")
            score_c += 1
        round_no += 1
    if score_p > score_c:
        print(f"\n🎉 You won the match! Final Score You:{score_p} CPU:{score_c}\n")
    else:
        print(f"\nCPU won the match. Final Score You:{score_p} CPU:{score_c}\n")
    input("Press Enter to return to menu...")

# ---------------------------
# Number Guessing
# ---------------------------
def number_guessing():
    print("\nNumber Guessing Game")
    low, high = 1, 100
    try:
        low = int(input("Enter lower bound (default 1): ") or 1)
        high = int(input("Enter upper bound (default 100): ") or 100)
        if low >= high:
            print("Invalid range. Using 1-100.")
            low, high = 1, 100
    except ValueError:
        print("Invalid input. Using 1-100.")
        low, high = 1, 100
    secret = random.randint(low, high)
    attempts = 0
    print(f"I've picked a number between {low} and {high}. Try to guess it!")
    while True:
        attempts += 1
        try:
            guess = int(input("Your guess: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess == secret:
            print(f"🎉 Correct! You guessed in {attempts} attempts.\n")
            break
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")
    input("Press Enter to return to menu...")

# ---------------------------
# Menu & Runner
# ---------------------------
def clear_screen():
    print("\n" * 2)

def main_menu():
    while True:
        clear_screen()
        print("=== Mini Games Pack ===")
        print("1) Tic-Tac-Toe (2-player)")
        print("2) Hangman")
        print("3) Rock-Paper-Scissors")
        print("4) Number Guessing")
        print("5) About / How to contribute")
        print("0) Quit")
        choice = input("Choose a game (0-5): ").strip()
        if choice == "1":
            tic_tac_toe()
        elif choice == "2":
            hangman()
        elif choice == "3":
            rps()
        elif choice == "4":
            number_guessing()
        elif choice == "5":
            print("""
About:
- This pack is simple and console-based so it's portable.
- To add to GitHub: create a repo, add this file, write README.md with instructions and screenshots (or GIF).
- Ideas to improve: add a GUI (Tkinter / Pygame), add AI for Tic-Tac-Toe (minimax), expand hangman dictionary, add multiplayer over network.
""")
            input("Press Enter to return to menu...")
        elif choice == "0":
            print("Thanks for playing — goodbye!")
            time.sleep(0.6)
            sys.exit(0)
        else:
            print("Invalid option. Try again.")
            time.sleep(0.6)

if __name__ == "__main__":
    main_menu()
