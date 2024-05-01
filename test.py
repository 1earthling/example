import json

def read_json(file_path):
    """Read JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_keys(data, prefix=''):
    """Recursively extract keys from nested JSON."""
    keys = set()
    if isinstance(data, dict):
        for k, v in data.items():
            new_prefix = f"{prefix}.{k}" if prefix else k
            keys.add(new_prefix)
            keys.update(extract_keys(v, new_prefix))
    elif isinstance(data, list):
        for item in data:
            keys.update(extract_keys(item, prefix))
    return keys

def compare_keys(file1, file2):
    """Compare keys from two JSON files and print the differences."""
    # Read and extract keys from both JSON files
    data1 = read_json(file1)
    data2 = read_json(file2)
    
    keys1 = extract_keys(data1)
    keys2 = extract_keys(data2)
    
    # Determine keys that are unique to each file
    unique_to_file1 = keys1 - keys2
    unique_to_file2 = keys2 - keys1
    
    # Output the results
    print("Keys unique to file1:", unique_to_file1)
    print("Keys unique to file2:", unique_to_file2)

# Example usage:
compare_keys('path/to/your/first_file.json', 'path/to/your/second_file.json')
