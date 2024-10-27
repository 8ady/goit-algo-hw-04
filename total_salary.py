def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            count = 0
            
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total_salary += int(salary)
                    count += 1
                except ValueError:
                    
                    print(f"Error processing line: '{line.strip()}', skipping...")
            
            
            if count == 0:
                return 0, 0

            
            average_salary = total_salary / count
            return total_salary, average_salary

    except FileNotFoundError:
        
        print(f"File not found at path '{path}'.")
        return 0, 0
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")
        return 0, 0


total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary sum: {total}, Average salary: {average}")
