
import requests

# =====================================
# YOUR OWN RENDER API URL
# =====================================

BASE_URL = "https://laud-gwyneth-joy1.onrender.com"


# =====================================
# STEP 1: ACCESS STUDENT ENDPOINT
# =====================================

print("\n===== STUDENT INFORMATION =====")

student_url = f"{BASE_URL}/student"

try:
    response = requests.get(student_url, timeout=60)

    if response.status_code == 200:

        data = response.json()

        print("Student ID:", data["student_id"])
        print("Name:", data["name"])
        print("Program:", data["program"])
        print("Year:", data["year"])
        print("Section:", data["section"])

    else:
        print("Request failed.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)


# =====================================
# STEP 2: ACCESS HELLO ENDPOINT
# =====================================

print("\n===== HELLO API =====")

name = input("Enter your first name: ")

hello_url = f"{BASE_URL}/hello"

params = {
    "name": name
}

try:
    response = requests.get(
        hello_url,
        params=params,
        timeout=60
    )

    if response.status_code == 200:

        data = response.json()

        print("Message:", data["message"])

    else:
        print("Request failed.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)


# =====================================
# STEP 3: ACCESS YOUR OWN NEW ENDPOINT
# SUBJECT INFORMATION
# =====================================

print("\n===== SUBJECT INFORMATION =====")

subject_url = f"{BASE_URL}/subject"

subject_params = {
    "code": "IT1101"
}

try:
    response = requests.get(
        subject_url,
        params=subject_params,
        timeout=60
    )

    if response.status_code == 200:

        data = response.json()

        print("Subject Code:", data["subject_code"])
        print("Subject Title:", data["title"])
        print("Semester:", data["semester"])
        print("Academic Year:", data["academic_year"])

    else:
        print("Request failed.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)


# =====================================
# END OF API CLIENT PROGRAM
# =====================================

print("\n===== API CLIENT PROGRAM COMPLETED =====")
