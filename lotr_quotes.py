from bs4 import BeautifulSoup
import requests
import re

url = "https://geektrippers.com/lord-of-the-rings-quotes-lines/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

quotes_raw = soup.find_all('p', class_='has-background')

pattern_1 = ":"
pattern_2 = "."
pattern_3 = r"a-zA-Z ?"
chars = []
quotes = []
movies = []
for quote in quotes_raw:
    sub_chars = []
    sub_quotes = []
    #print(quote.text)
    res = str(quote.text).replace("…", "...").replace('\xa0', ' ').replace("!","!.").replace("?","?.").replace("]","].")
    #print(res)
    splited_semicolumn = res.split(pattern_1) 
    sub_chars.append(splited_semicolumn[0].strip('“'))
    r = len(splited_semicolumn) -1
    if r <2 :
        sub_quotes.append(quote.text)
        movies.append(splited_semicolumn[-1])
    for i in range(1,r): 
        sub_text = splited_semicolumn[i]
        splited_dot = sub_text.rsplit(pattern_2, 1)
        #print(splited_dot, i , r)
        if len(splited_dot)==2 and i != r-1:
            sub_chars.append(splited_dot[1])
            sub_quotes.append(splited_dot[0])
    
        elif i==r-1 :
            if "Lord" in splited_dot[1]:
                sub_quotes.append(splited_dot[0])
                movies.append(splited_semicolumn[-1].strip(" "))

            else:

                sub_quotes.append(splited_dot[0])
                sub_chars.append(splited_dot[1])

                sub_quotes.append(splited_semicolumn[-1])
                movies.append(None)
            pass
            #print(splited_dot)
        else:
            print(splited_dot)
    quotes.append(sub_quotes)
    chars.append(sub_chars)
    # print("Quote:", res.strip())

# print(chars)
# print(quotes)
# print(movies)


# with open('all_quaotes_and_movies.txt', 'w') as file:
#     for inner_list in chars:
#         for item in inner_list:
#             file.write("%s === " % item)
#         file.write("\n")
# 
#     for item in movies:
#        file.write("%s\n" % item)
# 
#     for inner_list in quotes:
#         for item in inner_list:
#             file.write("%s " % item)
#         file.write("\n")


import random

# choose a random index from both lists
random_index = random.randint(0, len(quotes)-1)

# print the same inner indexes together in the same line
print("------------------------------")
for i in range(len(quotes[random_index])):
    print(f"{chars[random_index][i]} : {quotes[random_index][i]}.")

print("------------------------------")
print(f'--- "{movies[random_index]}" ---')
print("------------------------------")
