#!/usr/bin/env python3
"""
Main application file for the Branch Merge Lab
"""

def main():
    """Main function"""
    print("Welcome to Branch Merge Lab!")
    print("This is the UPDATED MAIN BRANCH version")
    
    # Basic functionality
    calculate_sum(5, 3)
    calculate_product(4, 7)
    calculate_difference(10, 3)

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

def calculate_difference(a, b):
    """Calculate difference of two numbers"""
    result = a - b
    print(f"Difference of {a} and {b} is: {result}")
    return result

if __name__ == "__main__":
    main()
