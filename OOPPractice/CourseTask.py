import datetime


class CourseTask:
    def __init__(self, title, category, due_date, points_earned, points_possible, completion_status):
        self.title = title
        self.category = category
        self.due_date = due_date
        self.points_earned = points_earned
        self.points_possible = points_possible
        self.completion_status = completion_status

    def information(self):
        print("Selected Task Information:\n"
              "-------------------------\n"
              f"Assignment: {self.title}\n"
              f"Category: {self.category}\n"
              f"Due: {self.due_date}\n"
              f"Status: {self.completion_status}")

    def update_completion(self):
        ans = input(f"Did you complete {self.title} y/n:   ")
        if ans != "n" and ans != "y":
            print("Your input is invalid, try again.")
        elif ans == 'y':
            self.completion_status = "Complete"
            print(f"This assignment is now marked {self.completion_status}.")
        elif ans == 'n':
            self.completion_status = self.completion_status
            print(f"This assignment is {self.completion_status}.")

    def update_score(self):
        ans = float(input("Points Scored on Assignment:  "))
        if ans > self.points_possible:
            print(
                f"You entered too many points! You can only score {self.points_possible} points on this assignment. Try again!")
            return
        else:
            self.points_earned = ans
            print(f"You earned {self.points_earned} points on this assignment.")

    def calculate_score(self):
        score = 0
        if self.points_earned is None:
            print("Please complete or enter points earned on this assignment.")
        else:
            score = (self.points_earned / self.points_possible) * 100
            print(f"Assignment Score: {score} %")

    def formatted(self):
        print(f"{self.title} ({self.category}) ---"
              f" {self.due_date.month}/{self.due_date.day}/{self.due_date.year} {self.due_date.hour}:{self.due_date.minute}: {self.due_date.second}"
              f"  - {self.completion_status} - {self.points_earned}/{self.points_possible} ")


def course_report(all_tasks):
    print("COURSE PROGRESS REPORT:\n"
          "-------------------------")
    for n in range(len(all_tasks)):
        print(f"Assignment: {all_tasks[n].title}\n"
              f"Category: {all_tasks[n].category}\n"
              f"Due: {all_tasks[n].due_date}\n"
              f"Status: {all_tasks[n].completion_status}\n"
              f"")
    print("-------------------------")


def main():
    task_1 = CourseTask("Calc II Lab #1", "Lab", datetime.datetime(2026, 9, 20, 23, 59, 59), None, 40, "Incomplete")
    task_2 = CourseTask("Calc II Chapter 8.1 WebAssign", "Assignment", datetime.datetime(2026, 9, 22, 23, 59, 59, ),
                        None, 50, "Incomplete")
    task_3 = CourseTask("Calc II Chapter 8 Reading Quiz", "Quiz", datetime.datetime(2026, 9, 23, 23, 59, 59), None, 50,
                        "Incomplete")
    task_4 = CourseTask("Calc II Project: Using Trig Sub", "Project", datetime.datetime(2026, 9, 22, 23, 59, 59), None,
                        120, "Incomplete")
    task_5 = CourseTask("Calc II Chapter 8 Reading", "Reading", datetime.datetime(2026, 9, 23, 23, 59, 59), None, 40,
                        "Incomplete")
    all_tasks = [task_1, task_2, task_3, task_4, task_5]
    course_report(all_tasks)
    task_2.information()
    task_1.update_completion()
    task_1.update_score()
    task_1.calculate_score()
    task_1.formatted()


main()