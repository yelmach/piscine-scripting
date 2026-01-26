def remember_the_apple(shopping_list):
    if not shopping_list or "apple" in shopping_list:
        return shopping_list
    else:
        shopping_list.append("apple")
        return shopping_list
