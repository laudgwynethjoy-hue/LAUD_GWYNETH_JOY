
import requests
import json

# Classmate's API endpoint
CLASSMATE_API_URL = "https://yvonne-mahilum.onrender.com/skills"

print("====================================")
print("       CLASSMATE API ")
print("====================================")

try:
    response = requests.get(CLASSMATE_API_URL, timeout=60)

    if response.status_code == 200:
        data = response.json()

        print("\n===== CLASSMATE API RESPONSE =====")

        if isinstance(data, dict):
            for key, value in data.items():
                print(f"{key.replace('_', ' ').title()}:")

                if isinstance(value, (dict, list)):
                    print(json.dumps(value, indent=4))
                else:
                    print(value)

        elif isinstance(data, list):
            print(json.dumps(data, indent=4))

        else:
            print(data)

        print("\nAPI connection successful!")

    else:
        print("\nRequest failed!")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

except requests.exceptions.RequestException as error:
    print("\nConnection error:", error)

except ValueError:
    print("\nThe API did not return valid JSON data.")

print("\n===== PROGRAM COMPLETED =====")
