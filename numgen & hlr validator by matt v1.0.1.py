import random
import tkinter as tk
from tkinter import filedialog
import requests

# Generate a random Australian mobile phone number with the same number of digits as +61 491 570 156, with the first five digits fixed as "+614", with an extra digit at the end, and without a space in the middle of the number
def generate_phone_number():
  # The first five digits should be +614
  first_five_digits = "+614"

  # The final eight digits can be any number from 0 to 9
  final_eight_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])

  return f"{first_five_digits}{final_eight_digits}"

# Display a banner with the title "NumGen and HLR Checker" using text art
print("""


███╗░░██╗██╗░░░██╗███╗░░░███╗░██████╗░███████╗███╗░░██╗    ░█████╗░███╗░░██╗██████╗░  
████╗░██║██║░░░██║████╗░████║██╔════╝░██╔════╝████╗░██║    ██╔══██╗████╗░██║██╔══██╗  
██╔██╗██║██║░░░██║██╔████╔██║██║░░██╗░█████╗░░██╔██╗██║    ███████║██╔██╗██║██║░░██║  
██║╚████║██║░░░██║██║╚██╔╝██║██║░░╚██╗██╔══╝░░██║╚████║    ██╔══██║██║╚████║██║░░██║  
██║░╚███║╚██████╔╝██║░╚═╝░██║╚██████╔╝███████╗██║░╚███║    ██║░░██║██║░╚███║██████╔╝  
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝    ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  


██╗░░██╗██╗░░░░░██████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██║░░░░░██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║██║░░░░░██████╔╝  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██║░░░░░██╔══██╗  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║███████╗██║░░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

█░█ ▄█ ░ █▀█   █▄▄ █▄█   █▀▄▀█ █▀█ ▀█▀ ▀█▀
▀▄▀ ░█ ▄ █▄█   █▄█ ░█░   █░▀░█ ▀▀█ ░█░ ░█░

Github: mqttAU
Discord: mqtt#0001
""")


# Prompt the user to choose whether to generate phone numbers or to perform HLR validation on a file
print("1. Generate AU Phone Numbers")
print("2. HLR Validator")
choice = input("What would you like to do?:")

# If the user wants to generate phone numbers
if choice == '1':
  # Open a file browser to select the file path to save the phone numbers
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.asksaveasfilename(defaultextension='.txt')

  # Prompt the user to enter the number of phone numbers they want to generate
  num_phone_numbers = int(input("Enter the number of phone numbers you want to generate: "))

  # Initialize an empty list to store the phone numbers
  phone_numbers = []

  # Generate the specified number of phone numbers without duplicates
  while len(phone_numbers) < num_phone_numbers:
    phone_number = generate_phone_number()
    if phone_number not in phone_numbers:
      phone_numbers.append(phone_number)

  # Save the phone numbers to the specified file
  with open(file_path, 'w') as f:
    f.write('\n'.join(phone_numbers))
    
    # Print a message indicating that the phone numbers were saved
  print(f"Generated and saved {len(phone_numbers)} phone numbers to {file_path}")

# If the user wants to perform HLR validation on a file
elif choice == '2':
  # Open a file browser to select the file containing the phone numbers
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename()

  # Read the phone numbers from the file
  with open(file_path, 'r') as f:
    phone_numbers = f.read().splitlines()

  # Perform HLR validation on the phone numbers
  validated_phone_numbers = []
  for phone_number in phone_numbers:
    # Send an HLR validation request for the phone number using the NumVerify API
    r = requests.get(f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}")

    # Get the carrier, line type, country code, and validity information for the phone number
    carrier = r.json()["carrier"]
    line_type = r.json()["line_type"]
    country_code = r.json()["country_code"]
    validity = "Valid" if r.json()["valid"] else "Invalid"

    # Add the phone number, carrier, line type, country code, and validity information to the list of validated phone numbers
    validated_phone_numbers.append(f"{phone_number},{carrier},{line_type},{country_code},{validity}")

  # Save the validated phone numbers to the specified file
  with open(file_path, 'w') as f:
    f.write('\n'.join(validated_phone_numbers))

  # Print a message indicating that the phone numbers were saved
  print(f"Performed HLR validation on and saved {len(validated_phone_numbers)} phone numbers to {file_path}")

# If the user entered an invalid choice
else:
  print("Invalid choice. Please try again.")