#In the specified playback.py file, you're tasked to create a Python program that prompts the user for input, then outputs the same input but replaces each space with three periods (...). This simulates a slowed down or paused playback, similar to YouTube's 0.75 playback speed feature, by adding pauses between words.

user_input = input("")
modified_user_input = user_input.replace(" ", "...")

print(modified_user_input)