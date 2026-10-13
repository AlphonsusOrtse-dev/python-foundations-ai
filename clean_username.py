def clean_username(value):
    # Remove leading and trailing spaces
    username = value.strip()

    # Convert all letters to lowercase
    username = username.lower()

    # Replace every space with an underscore
    username = username.replace(" ", "_")

    # Return the cleaned username
    return username


print(clean_username("  ALICE  "))
print(clean_username("Mary Jane Watson"))  
print(clean_username("ALPHONSUS"))  
print(clean_username(""))
print(clean_username(" John "))  
print(clean_username("John   Doe"))  