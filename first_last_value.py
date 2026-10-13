def first_and_last(value):
    # Check if the string is empty
    if value == "":
        # Return empty strings for both keys
        return {"first": "", "last": ""}
    else:
        # Get the first character using index 0
        # Get the last character using index -1
        return {"first": value[0], "last": value[-1]}
    
print(first_and_last("Python"))
print(first_and_last("A"))
print(first_and_last(""))