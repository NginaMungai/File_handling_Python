try:
  with open("my_file.txt", "w") as file:
    # Write content to the file
    file.write("Hello World! This is some text written to the new file. \n")
    file.write("42/2 \n")
    file.write("The answer is 21! \n")
  print("File 'my_file.txt' created successfully!")
except FileNotFoundError:
  print("Error: Could not create file 'my_file.txt'.")
except PermissionError:
  print("Error: Insufficient permissions to create 'my_file.txt'.")
except Exception as e:
  print(f"An error occurred while creating the file: {e}")

try:
  with open("my_file.txt", "r") as file:
    # Read the contents of the file
    file_content = file.read()

  # Print the contents of the file
  print("Contents of 'my_file.txt':")
  print(file_content)

  print("File read successfully!")
except FileNotFoundError:
  print("Error: File 'my_file.txt' not found.")
except PermissionError:
  print("Error: Insufficient permissions to read 'my_file.txt'.")
except Exception as e:
  print(f"An error occurred while reading the file: {e}")

try:
  with open("my_file.txt", "a") as file:
    # Append three lines of text to the file
    file.write("Hello World! This is some text written to the new file. Kindly read through it. \n")
    file.write("42/2, 21/3 \n")
    file.write("The answer is 21 and 7 respectively! ")

  print("Successfully appended content to 'my_file.txt'!")
except FileNotFoundError:
  print("Error: File 'my_file.txt' not found for appending.")
except PermissionError:
  print("Error: Insufficient permissions to append to 'my_file.txt'.")
except Exception as e:
  print(f"An error occurred while appending to the file: {e}")
