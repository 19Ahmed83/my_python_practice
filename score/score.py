import emoji
score =int(input("Score: "))
if 89 <= score <= 100:
    print("You win: ", end = "")
    print((emoji.emojize(":1st_place_medal:", language = "alias")))

elif  79 <= score <= 88:
    print("You second: ", end = "")
    print(emoji.emojize(":2nd_place_medal:", language = "alias"))

else:
    print("You third: ", end = "")
    print(emoji.emojize(":3rd_place_medal:", language = "alias"))        