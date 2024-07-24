def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)

def extract_codes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.strip() for line in file}

def filter_lines(file1_lines, codes):
    filtered_lines = []
    for line in file1_lines:
        code = line.split()[0]
        if code in codes:
            filtered_lines.append(line)
    return filtered_lines

def main():
    file1_path = 'produtos_estoque.txt'
    file2_path = 'produtos_solicitados.txt'
    output_path = 'arquivo_filtrado.txt'

    file1_lines = read_file(file1_path)
    codes = extract_codes(file2_path)
    filtered_lines = filter_lines(file1_lines, codes)
    write_file(output_path, filtered_lines)

if __name__ == "__main__":
    main()
