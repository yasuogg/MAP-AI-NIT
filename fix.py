import os

def fix_detection_results_file(file_path, default_confidence=0.9):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            parts = line.split()
            if len(parts) == 5:
                class_name, left, top, right, bottom = parts
                new_line = f"{class_name} {default_confidence} {left} {top} {right} {bottom}\n"
                file.write(new_line)
            else:
                file.write(line)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            fix_detection_results_file(file_path)
            print(f"Processed {file_path}")

# Example usage
folder_path = "/Users/cex/api nit /MAP/ code/mAP/input/detection-results"
process_folder(folder_path)
