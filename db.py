import os
# Convert format
tsv_files = [f for f in os.listdir('.') if f.endswith('.tsv')]

if 'data.tsv' not in tsv_files:
    if not tsv_files:
        print("No .tsv files found in the current directory.")
    else:
        print("Available .tsv files:")
        for idx, filename in enumerate(tsv_files):
            print(f"{idx + 1}: {filename}")
        
        try:
            choice = int(input("Enter the number of the file: ")) - 1
            if 0 <= choice < len(tsv_files):
                selected_file = tsv_files[choice]
            else:
                print("Invalid choice. Exiting.")
                exit()
        except ValueError:
            print("Invalid input. Exiting.")
            exit()
else:
    selected_file = 'data.tsv'

with open(selected_file, 'r') as file:
    lines = file.readlines()

formatted_data = {}

for line in lines:
    columns = line.strip().split('\t')
    if len(columns) == 4:
        key = columns[1]
        value = columns[3]
        if key in formatted_data:
            formatted_data[key].append(value)
        else:
            formatted_data[key] = [value]

with open('data.db', 'w') as output_file:
    for key, values in formatted_data.items():
        for value in values:
            output_file.write(f'{key}={value}\n')

print("Formatting completed.")
