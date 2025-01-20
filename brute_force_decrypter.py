# Module imports.
from pathlib import Path
from pypdf import PdfReader, errors

# Plan
# Iterate through PDF files with globby glob glob.
# Skip decrypted files.
# Iterate through dictionary.txt
# Attempt decryption using upper and lowercase version of each word.
# Print out password if decryption is successful and move onto next file.

# Prompts user for folder and validates input.
# pdf = Path(input("PDF file to brute force:\n"))

# NOTE: Variable for quicker testing. DELETE ONCE FINISHED.
pdf = Path(r'C:\Users\Manka\Documents\Programming\Automate the Boring Stuff with Python\Chapter 15 - Working with PDF and Word documents\brute_force_pdf_password_breaker\encrypted.pdf')

if not pdf.is_file() and pdf.suffix != '.pdf':
    print("ERROR - INVALID DIRECTORY!")
    quit()

# Prompts user for password text file and validates input.
# text_file = Path(input("\nText file storing password attempts:\n"))

# NOTE: Variable for quicker testing. DELETE ONCE FINISHED.
text_file = Path(r'C:\Users\Manka\Documents\Programming\Automate the Boring Stuff with Python\Chapter 15 - Working with PDF and Word documents\brute_force_pdf_password_breaker\dictionary.txt')

if not text_file.is_file() and text_file.suffix != '.txt':
    print("ERROR - VALID TEXT FILE NOT PROVIDED!")
    quit()

reader = PdfReader(pdf)
count = 0

with open(text_file) as fhandle:
    passwords = fhandle.readlines()

if reader.is_encrypted:
    for word in passwords:
        count += 1
        if reader.decrypt(word.lower().strip()):
            print(f'\r\n\n{pdf} CRACKED\n\nPASSWORD: {word.lower().strip()}')
            break
        elif reader.decrypt(word.upper().strip()):
            print(f'\r\n\n{pdf} CRACKED\n\nPASSWORD: {word.upper().strip()}')
            break
        print(f'\r{round((count/len(passwords)) * 100, 2)}%', flush=True, end="")