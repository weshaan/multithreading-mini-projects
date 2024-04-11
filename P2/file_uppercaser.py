def convert_to_uppercase(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        content_upper = content.upper()

        with open(file_name, 'w') as file:
            file.write(content_upper)

        print("Conversion successful.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print("An error occurred:", e)

file_name = "example.txt"
convert_to_uppercase(file_name)
