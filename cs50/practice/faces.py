"""
Project Name: Faces
Purpose: Replaces basic text emoticons like ':)' and ':(' with actual emoji in user input
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
text = input("whats up? ")
text = text.replace(":)", "🙂")
text = text.replace(":(", "🙁")
print(text)
