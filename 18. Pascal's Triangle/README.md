# ⭐ Python Pascal's Triangle Function Demonstration ⭐

Welcome to the Python Pascal's Triangle Function Demonstration! This script showcases a function that prints Pascal's Triangle based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, conditional logic, and mathematical calculations.

## Script Overview 📘

The script includes a function called `pascal_triangle` which takes an integer `n` and prints Pascal's Triangle with `n` rows. The script demonstrates how to use nested loops to generate and format the output, along with calculating binomial coefficients.

### :computer: Script Code

```python
def pascal_triangle(n):
    for i in range(n):
        # Print leading spaces
        for j in range(n - i + 1):
            print(" ", end="")
        # Calculate and print binomial coefficients
        c = 1
        for j in range(1, i + 1):
            print(c, end=" ")
            c = c * (i - j) // j
        print()

def main():
    n = int(input("Please give me a integer: "))
    pascal_triangle(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Looping Constructs**: Learn how to use nested loops to create complex patterns and shapes.
- **Mathematical Calculations**: Understand how to calculate binomial coefficients to generate Pascal's Triangle.
- **String Formatting**: Learn how to format strings to align characters and create visually appealing output.

# Console Output Example 📋
When you run the script and input 5, the console output will be:

```python
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `pascal_triangle.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `pascal_triangle.py`.
5. Run the script with: `python pascal_triangle.py`.

# Usage Example 📋
Execute the script, input an integer value when prompted, and see how the function generates Pascal's Triangle with the specified number of rows. This will help you understand the practical applications of nested loops, formatted string output, and mathematical calculations in Python programming.

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