# Module imports.
from pathlib import Path
from pypdf import PdfReader

# Prompts user for folder and validates input.
pdf = Path(input("PDF file to brute force:\n"))
if not pdf.is_file() and pdf.suffix != '.pdf':
    print("ERROR - INVALID DIRECTORY!")
    quit()

# Prompts user for password text file and validates input.
text_file = Path(input("\nText file storing password attempts:\n"))
if not text_file.is_file() and text_file.suffix != '.txt':
    print("ERROR - VALID TEXT FILE NOT PROVIDED!")
    quit()

# Variable initilisation.
reader = PdfReader(pdf)
count = 0
with open(text_file) as fhandle:
    passwords = fhandle.readlines()

if reader.is_encrypted:
    for word in passwords:
        count += 1

        # Attempts decryption with word variations.
        if reader.decrypt(word.lower().strip()):
            print(f'\n\n{pdf} CRACKED\n\nPASSWORD: {word.lower().strip()}')
            break
        elif reader.decrypt(word.upper().strip()):
            print(f'\n\n{pdf} CRACKED\n\nPASSWORD: {word.upper().strip()}')
            break

        # Tracks progress of password attempts.
        print(f'\r{round((count/len(passwords)) * 100, 2)}%', flush=True, end="")