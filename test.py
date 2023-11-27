def create_test_file():
    file_name = input("Enter the file name for the test file: ")
 
    file_extension = input("Enter the file extension (e.g., txt, csv, etc.): ")
    if not file_extension.startswith('.'):
        file_extension = '.' + file_extension
 
    full_file_name = file_name + file_extension
 
    try:
        with open(full_file_name, 'w') as file:
            file.write("This is a test file created by the script.")
        print(f"Test file '{full_file_name}' has been created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
 
if __name__ == "__main__":
    create_test_file()
