### Basic dictionary

teen_dict = {
    'hc': 'Học, Hành động học tập, tiếp thu tri thức của con người.',
    'ng': 'Người, Nói về con người, một người nào đó hoặc nói chung về loài người',
    'pt': 'Phát triển, Biết một điều gì đó..., phát triển một cái gì đó.... ',
    'eny': 'Em người yêu',
    'any': 'Ánh người yêu',
    'ns': 'Nói',
    'ngta': 'Người ta, Người ta (ý nói một người khác, không liên quan tới mình)',
    'lm': 'Làm, Ý nói làm một việc gì đó, lắm (một từ trong câu)',
    'r': 'Rồi, Ý nói đã xong một việc gì đó',
    'stt': 'Status, trạng thái cảm xúc hiện tại'
}

while True:
    for key in teen_dict:
        print(key, end='\t')
    print()

    code = input("Your code? ")
    print("* " * 20)

    if code in teen_dict:
        print("Code:", code)
        print("Translation:", teen_dict[code])
    else:
        choice = input("Not found, do you want to contribute this word? (Y/N)? ")
        if choice.upper() == "Y":
            tranlation = input("Enter your tranlation: ")
            teen_dict[code] = tranlation
            print("Updated")
        else:
            break


    print("* " * 20)
