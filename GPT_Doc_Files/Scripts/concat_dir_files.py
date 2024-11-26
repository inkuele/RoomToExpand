import os
import sys

def read_and_write_files(folder, out_file, base_folder):
    # Iterate through each item in the folder
    for item in sorted(os.listdir(folder)):  # Sort to maintain a consistent order
        item_path = os.path.join(folder, item)

        # Calculate the relative path from the base folder
        relative_path = os.path.relpath(item_path, base_folder)

        # If it's a file, read it in binary mode and keep only ASCII characters
        if os.path.isfile(item_path):
            out_file.write(f"<{relative_path}>\n\n")
            with open(item_path, 'rb') as in_file:
                content = in_file.read().decode('ascii', errors='ignore')
                out_file.write(content + "\n")
            out_file.write("\n" + "-" * 30 + "\n\n")

        # If it's a folder, recursively call this function
        elif os.path.isdir(item_path):
            read_and_write_files(item_path, out_file, base_folder)

def concatenate_files_in_directory(dir_path):
    # Get the directory name and create output file path in the parent directory
    dir_name = os.path.basename(dir_path)
    output_file_name = f"{dir_name.replace('.dir', '')}.txt"
    parent_directory = os.path.dirname(os.path.dirname(__file__))
    output_file_path = os.path.join(parent_directory, output_file_name)
    
    # Open the output file in write mode
    with open(output_file_path, 'w') as out_file:
        read_and_write_files(dir_path, out_file, dir_path)
    
    print(f"Files concatenated into {output_file_path}")

if __name__ == "__main__":
    # Check if a directory path argument is provided
    if len(sys.argv) < 2:
        print("Usage: python concatenate.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        print("The provided path is not a directory.")
        sys.exit(1)
    
    # Run the concatenation function
    concatenate_files_in_directory(directory_path)

