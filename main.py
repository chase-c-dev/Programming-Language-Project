from tokenizing import tokenize

def main():
    srcCode = "123 + 55 + 65"
    final_list = tokenize(srcCode)
    for item in final_list:
        print(item)

main()