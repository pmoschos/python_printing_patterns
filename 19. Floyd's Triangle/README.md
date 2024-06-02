# ⭐ Python Floyd's Triangle Function Demonstration ⭐

Welcome to the Python Floyd's Triangle Function Demonstration! This script showcases a function that prints Floyd's Triangle based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, conditional logic, and number sequences.

## Script Overview 📘

The script includes a function called `floyd_triangle` which takes an integer `n` and prints Floyd's Triangle with `n` rows. The script demonstrates how to use nested loops to generate and format the output, along with incrementing numbers in a sequential manner.

### :computer: Script Code

```python
def floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

def main():
    n = int(input("Please give me a integer: "))
    floyd_triangle(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Looping Constructs**: Learn how to use nested loops to create complex patterns and shapes.
- **Number Sequences**: Understand how to generate and print sequential numbers in a structured pattern.
- **String Formatting**: Learn how to format strings to align characters and create visually appealing output.

# Console Output Example 📋
When you run the script and input 7, the console output will be:

```python
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `floyd_triangle.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `floyd_triangle.py`.
5. Run the script with: `python floyd_triangle.py`.

# Usage Example 📋
Execute the script, input an integer value when prompted, and see how the function generates Floyd's Triangle with the specified number of rows. This will help you understand the practical applications of nested loops, formatted string output, and number sequences in Python programming.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>