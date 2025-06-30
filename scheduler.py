def display_menu():
    print("\nSmart Scheduler Menu")
    print("1. Add a new exam")
    print("2. View all exams")
    print("3. Edit an exam entry")
    print("4. Delete an exam entry")
    print("5. Exit")

def add_exam(exams):
    
    print("\nAdd New Exam")
    exam_name = input("Enter exam name: ").strip()
    exam_date = input("Enter date (YYYY-MM-DD): ").strip()
    exam_time = input("Enter time (HH:MM AM/PM): ").strip()
    exam_room = input("Enter assigned room (e.g. abc27): ").strip()
    
    if not all([exam_name, exam_date, exam_time]):
        print("Error: Exam not added.")
        return

    exam = {
        "name": exam_name,
        "date": exam_date,
        "time": exam_time, 
        "room": exam_room
    }
    exams.append(exam)
    print(f"Exam '{exam_name}' added successfully!")

def view_exams(exams):
    
    print("\nAll Exams")
    if not exams:
        print("No exams scheduled yet.")
        return

    print(f"{'No.':<4} | {'Exam Name':<30} | {'Date':<12} | {'Time':<15} | {'Room':<15}")
    print("-" * 80)

    for i, exam in enumerate(exams):
        print(
            f"{i + 1:<4} | {exam['name']:<30} | {exam['date']:<12} | "
            f"{exam['time']:<15} | {exam['room']:<15}"
        )
    print("-" * 80)

def edit_exam(exams):
    
    print("\nEdit Exam")
    if not exams:
        print("No exams to edit.")
        return

    view_exams(exams)
    try:
        exam_index = int(input("Enter the number of the exam to edit: ")) - 1
        if 0 <= exam_index < len(exams):
            current_exam = exams[exam_index]
            print(f"\nEditing exam: {current_exam['name']}")
            print("Press Enter to keep current value.")

            new_name = input(f"Enter new exam name ({current_exam['name']}): ").strip()
            if new_name:
                current_exam['name'] = new_name

            new_date = input(f"Enter new date ({current_exam['date']}): ").strip()
            if new_date:
                current_exam['date'] = new_date

            new_time = input(f"Enter new time ({current_exam['time']}): ").strip()
            if new_time:
                current_exam['time'] = new_time
                
            new_room = input(f"Enter new room ({current_exam['room']}): ").strip()
            if new_room:
                current_exam['room'] = new_room

            print("Exam updated successfully!")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_exam(exams):
    
    print("\nDelete Exam")
    if not exams:
        print("No exams to delete.")
        return

    view_exams(exams)
    try:
        exam_index = int(input("Enter the number of the exam to delete: ")) - 1
        if 0 <= exam_index < len(exams):
            deleted_exam = exams.pop(exam_index)
            print(f"Exam '{deleted_exam['name']}' deleted successfully!")
        else:
            print("Invalid exam number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    
    exams = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_exam(exams)
        elif choice == '2':
            view_exams(exams)
        elif choice == '3':
            edit_exam(exams)
        elif choice == '4':
            delete_exam(exams)
        elif choice == '5':
            print("Exiting Smart Scheduler")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
