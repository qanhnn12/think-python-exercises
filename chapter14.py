# EXERCISE 14.1
def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()

def main():
    pattern = "cant"
    replace = "can't"
    source = 'words.txt'
    dest = 'new_file.txt'

if __name__ == '__main__':
    main()
