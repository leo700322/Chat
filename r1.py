# read file
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

# convert format
def convert(lines):
    new = []
    person = None # 預設值
    for line in lines:
        if 'Allen' in line:
            person = 'Allen'
            continue
        elif 'Tom' in line:
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line) # 不能用 lines = new.append(person + ': ' + line) 取代第34行，因為 function 內部 lines 參數的變更，只對 function 內部有效，不能回傳到外部!
    return new 

# write file
def write_file(filename, lines):
    with open (filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

# main function
def main():
    lines = read_file('input.txt')
    lines = convert(lines) # 將convert 的結果取代成上一行的 lines
    write_file('output.txt', lines)

main()