a =["darshan is the best engineering college in rajkot",
 "rajkot is famous for engineering",
 "college is located in rajkot mardiroad"]
from sklearn.feature_extraction.text import *
countVector = CountVectorizer()
X_train_counts =countVector.fit_transform(a)
print(countVector.vocabulary_)
print(X_train_counts.toarray( ) )


%%timeit -n -r 7
for i in range(2,1000) :
   listPrime =[]
   flag=0
   for j in range(2,i) :
       if i%j==0:
           flag =1
           break
       if flag == 0:
           listPrime . append (i)
#pritnt(ListPrime )