import os

# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Function to generate and display report cards
def generate_report_card(students):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for a clean output
    print("\n📜 STUDENT REPORT CARDS 📜")
    print("=" * 50)

    for student in students:
        print(f"\n📝 Report Card for: {student['Name']}  (Roll No: {student['Roll No']})")
        print("=" * 50)
        print(f"{'Subject':<15}{'Marks':<10}{'Grade':<5}")
        print("-" * 50)

        total_marks = 0
        for subject, marks in student["Subjects"].items():
            grade = calculate_grade(marks)
            print(f"{subject:<15}{marks:<10}{grade:<5}")
            total_marks += marks

        percentage = total_marks / 5  # Since we have 5 subjects
        final_grade = calculate_grade(percentage)

        print("-" * 50)
        print(f"Total Marks: {total_marks}/500")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Overall Grade: {final_grade}")
        print("=" * 50)

# Main function to handle user input
def main():
    students = []

    while True:
        print("\n📌 Enter Student Details:")
        name = input("Student Name: ")
        roll_no = input("Roll Number: ")

        subjects = {}
        subjects["Math"] = float(input("Math Marks: "))
        subjects["Physics"] = float(input("Physics Marks: "))
        subjects["Urdu"] = float(input("Urdu Marks: "))
        subjects["English"] = float(input("English Marks: "))
        subjects["Computer"] = float(input("Computer Marks: "))

        students.append({"Name": name, "Roll No": roll_no, "Subjects": subjects})

        print(f"\n✅ Record of {name} inserted successfully!")
        choice = input("Do you want to insert more? (Press 'Y' for Yes or 'N' for No): ").strip().upper()
        
        if choice == 'N':
            break

    generate_report_card(students)

# Run the program
if __name__ == "__main__":
    main()
