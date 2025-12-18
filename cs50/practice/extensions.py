"""
Project Name: FExtensions
Purpose: Prompts the user for a file name and prints its corresponding MIME type based on the file extension
Author: Jessica Rust
Course/Source: cs50
Date: 12/18/2025
"""
def main():
    file_name = input("File name: ").lower().strip()

    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print ("application/octet-stream")

main()
