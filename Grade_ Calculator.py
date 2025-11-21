def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def get_valid_mark(subject_name):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def display_result(student_name, marks, total, average, grade):
    print("\n" + "="*50)
    print("STUDENT GRADE REPORT")
    print("="*50)
    print(f"Student Name: {student_name}")
    print("-"*50)
    
    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    for i, subject in enumerate(subjects):
        print(f"{subject}: {marks[i]:.2f}")
    
    print("-"*50)
    print(f"Total Marks: {total:.2f}")
    print(f"Average: {average:.2f}%")
    print(f"Grade: {grade}")
    print("="*50)

def main():
    print("Welcome to the Student Grade Calculator!")
    print("-" * 40)
    
    student_name = input("Enter student's name: ").strip()
    
    marks = []
    for i in range(1, 4):
        mark = get_valid_mark(f"Subject {i}")
        marks.append(mark)
    
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    
    display_result(student_name, marks, total, average, grade)
    
    while True:
        another = input("\nWould you like to calculate for another student? (y/n): ").lower()
        if another in ['y', 'yes']:
            print("\n" + "-"*40)
            main()
            break
        elif another in ['n', 'no']:
            print("Thank you for using the Grade Calculator!")
            break
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()

