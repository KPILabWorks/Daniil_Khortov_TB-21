def bracketsChecker(text):
    bracketsDict = {'(': ')', '[': ']', '{': '}'}
    
    stack = []
    
    for symbol in text:
        if symbol in bracketsDict:
            stack.append(symbol)
        elif symbol in bracketsDict.values():
            if not stack or bracketsDict[stack.pop()] != symbol:    
                return False
            
    
    if len(stack) == 0:
        print("⠄⠄⠄⠄⠄⠄⠄⢀⣀⣠⣤⠴⠶⠶⠶⠶⠶⠶⠶⢤⣄⣀⡀⠄⠄⠄⠄⠄⠄⠄\n"+
            "⠄⠄⠄⠄⠄⣠⣶⠟⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠶⣄⡀⠄⠄⠄⠄\n"+
            "⠄⠄⠄⣠⡾⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣆⠄⠄⠄\n"+
            "⠄⠄⣼⡟⠄⠄⠄⠄⠄⠄⠄⢀⣤⣶⡶⢦⡀⠄⠄⠄⠄⠄⠄⠖⠻⣶⠞⢧⠄⠄\n"+
            "⠄⣼⠏⠄⠄⠄⠄⠄⠄⠄⠐⠛⠋⠁⠄⠄⠄⠄⠄⠄⠄⢀⣤⣤⣄⠄⠄⠨⣧⠄\n"+
            "⢸⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⡏⠄⠄⠄⠸⡇\n"+
            "⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡄⠄⠰⠄⠄⠄⠄⠄⢀⡇⠄⢀⡘⢣⣿\n"+
            "⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣄⠄⠄⠦⠄⢀⣠⣤⣶⣿⠿⣶⣦⣴⠟⢹\n"+
            "⢿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠛⠛⠛⠉⠁⠄⠄⠄⠄⠜⠁⠄⣾\n"+
            "⠈⢧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⠇\n"+
            "⠄⠈⠑⢄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡴⠋⠄\n"+
            "⠄⠄⠄⠄⠐⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⡴⠏⠄⠄⠄\n"+
            "⠄⠄⠄⠄⠄⠄⠄⠄⠐⠂⠤⠤⣄⣀⣀⣀⣠⣤⣤⣤⡶⠶⠟⠋⠁⠄⠄⠄⠄⠄\n")

        return True
    else:
        return False

textInput = input()
print(bracketsChecker(textInput))
