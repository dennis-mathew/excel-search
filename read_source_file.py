def read_source_file(file_name):
    # Initialize an empty dictionary to store the key-value pairs
    data_dict = {}

    # Open and read the colon-separated file
    with open(file_name, 'r') as file:
        for line in file:
            # Split each line into key and value using the colon (':') as a separator
            key, value = line.strip().split(':', 1)
            
            # Store the key-value pair in the dictionary
            data_dict[key.strip()] = value.strip()
    return data_dict
