import json

try:
    data = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "courses": ["Math", "Science", "History"],
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "zip": "12345"
        }}

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    with open('datas.json', 'r') as infile:
        loaded_data = json.load(infile)
        print(loaded_data)

except FileNotFoundError as e:
    print("File not found:", e)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
except Exception as e:
    print("An error occurred:", e)