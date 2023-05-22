import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import language_tool_python

nltk.tokenize.punkt

A = input("Enter first string: ")
B = input("Enter second string: ")

X = A.lower()
Y = B.lower()

X_list = word_tokenize(X)
Y_list = word_tokenize(Y)

sw = stopwords.words('english')
l1 = [];l2 = []

X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}

rvector = X_set.union(Y_set)
for w in rvector:
    if w in X_set:
        l1.append(1)
    else:
        l1.append(0)
    if w in Y_set:
        l2.append(1)
    else:
        l2.append(0)
c = 0

for i in range(len(rvector)):
    c += l1[i] * l2[i]
cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
print("similarity: ", cosine)

my_tool = language_tool_python.LanguageTool('en-US')
my_text1 = B

my_matches1 = my_tool.check(my_text1)

len(my_matches1)
print(len(my_matches1))
if len(my_matches1) <= 5:
    print("Least Error")
elif len(my_matches1) > 5 and len(my_matches1) <= 10:
    print("Medium Error")
else:
    print("Maximum Error")