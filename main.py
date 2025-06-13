#!/usr/bin/env python3
"""
Main application file for the Branch Merge Lab
"""

def main():
    """Main function"""
    print("Welcome to Branch Merge Lab!")
    print("This is the initial version on main branch")
    
    # Basic functionality
    calculate_sum(5, 3)
    calculate_product(4, 7)

def calculate_sum(a, b):
    """Calculate sum of two numbers"""
    result = a + b
    print(f"Sum of {a} and {b} is: {result}")
    return result

def calculate_product(a, b):
    """Calculate product of two numbers"""
    result = a * b
    print(f"Product of {a} and {b} is: {result}")
    return result

def calculate_division(a, b):
    """Calculate division of two numbers"""
    if b == 0:
        print("Error: Division by zero!")
        return None
    result = a / b
    print(f"Division of {a} by {b} is: {result}")
    return result

if __name__ == "__main__":
    main()
