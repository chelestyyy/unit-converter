def get_input_value():
    while True:
        try:
            return float(input("Enter the value to convert: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_conversion():
    print("\nSelect Conversion:")
    print("1. Unit 1 to Unit 2")
    print("2. Unit 1 to Unit 3")
    print("3. Unit 2 to Unit 3")
    
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice. Please try again.")

def convert_unit(value, conversion_type):
    # Placeholder conversion factors - replace these with actual conversion factors
    if conversion_type == 1:
        return value * 2, "Unit 1", "Unit 2"  # Unit 1 to Unit 2
    elif conversion_type == 2:
        return value * 3, "Unit 1", "Unit 3"  # Unit 1 to Unit 3
    elif conversion_type == 3:
        return value * 1.5, "Unit 2", "Unit 3"  # Unit 2 to Unit 3

def unit_converter():
    print("Welcome to the Unit Converter")
    
    # Get input value
    input_value = get_input_value()
    
    # Select conversion
    conversion_type = select_conversion()
    
    # Perform conversion
    converted_value, from_unit, to_unit = convert_unit(input_value, conversion_type)
    
    # Display result
    print(f"\n{input_value} {from_unit} is equal to {converted_value} {to_unit}")

# Run the unit converter
unit_converter()
