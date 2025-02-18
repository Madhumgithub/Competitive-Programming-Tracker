
### **🐍 script.py**
```python
import json

# Load existing data
try:
    with open("problems.json", "r") as file:
        problems = json.load(file)
except FileNotFoundError:
    problems = []

while True:
    platform = input("Enter platform (LeetCode/CodeChef/Codeforces): ")
    problem = input("Enter problem name: ")
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ")
    problems.append({"platform": platform, "problem": problem, "difficulty": difficulty})
    
    if input("Add another? (yes/no): ").lower() != "yes":
        break

# Save data
with open("problems.json", "w") as file:
    json.dump(problems, file, indent=4)

print("\nProblem List Saved Successfully!")
