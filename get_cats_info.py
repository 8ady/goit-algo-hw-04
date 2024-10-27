file_path = "cats_file.txt"
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    file.write("60b90c2413067a15887e1ae2,Vika,1\n")
    file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    file.write("60b90c4613067a15887e1ae5,Tessi,5\n")


def get_cats_info(path):
    cats_info = []
    
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                
                try:
                    cat_id, name, age = line.strip().split(',')
                    
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Error processing line: '{line.strip()}', skipping...")

    except FileNotFoundError:
        print(f"File not found at path '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return cats_info


cats_info = get_cats_info(file_path)
print(cats_info)
