# daily_reminder.py

# Prompt for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate input with a loop if needed (optional but recommended)
while priority not in ["high", "medium", "low"]:
    print("Please enter a valid priority (high, medium, or low).")
    priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ["yes", "no"]:
    print("Please answer with yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to provide customized response
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Plan to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to fit it into your schedule.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but still needs to be done today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
