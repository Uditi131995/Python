secret_word = "tiger"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != secret_word and not out_of_guess:   # User word!=Right Word and out_of_guess=false
    if guess_count < guess_limit:
        guess = input("Enter the guess:")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guess, You lose")
else:
    print("You win")

