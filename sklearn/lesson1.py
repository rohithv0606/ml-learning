import pandas as pd
import numpy as np
from sklearn.datasets import load_iris   
from sklearn.neighbors import KNeighborsClassifier
#data representation
iris = load_iris()
X=iris.data
y=iris.target

#common steps in machine learning
# step 1: create model
model=KNeighborsClassifier(n_neighbors=3) 

# step 2: train model
model.fit(X,y)      

new_flowers = [[5.1, 3.5, 1.4, 0.2],
               [5.9, 3.0, 4.2, 1.5],
               [6.5, 3.0, 5.5, 1.8]]

# step 3: make predictions
predict=model.predict(new_flowers)

print(predict) #gives the index of the predicted class
print(iris.target_names[predict]) #gives the name of the predicted class

#****EXERCISE:****
# 1.Print the shape of X and y, and write a comment explaining in your own words what each number means.
# 2.Print how many flowers are in each class, using value_counts() on the DataFrame or np.unique(y, return_counts=True).
# 3.Make up 2 new flowers (try values close to the examples, and also some strange ones like [1, 1, 1, 1]) and predict their species.
# 4.Change n_neighbors to 1, then to 15, and see whether any predictions change. Think about why K = 1 (only the single closest flower decides) could be risky.
# 5.Deliberately predict with a flat list [5.1, 3.5, 1.4, 0.2] and read the error message. Then fix it.

#***ANSWERS:***
# 1. Shapes
print(X.shape)   # (150, 4)
print(y.shape)   # (150,)
# X: 150 samples (rows, flowers) and 4 features (columns, measurements)
# y: 150 answers, one species number per flower

# 2. Count of each class
print(np.unique(y, return_counts=True))
# (array([0, 1, 2]), array([50, 50, 50]))

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = iris.target_names[y]
print(df["species"].value_counts())   # 50 of each

# 3. Predict new flowers
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

new_flowers = [[5.1, 3.5, 1.4, 0.2],
               [5.9, 3.0, 4.2, 1.5],
               [6.5, 3.0, 5.5, 1.8],
               [1, 1, 1, 1]]
preds = model.predict(new_flowers)
print(iris.target_names[preds])
# ['setosa' 'versicolor' 'virginica' 'setosa']

# 4. Different K values
for k in [1, 3, 15]:
    m = KNeighborsClassifier(n_neighbors=k)
    m.fit(X, y)
    print(k, iris.target_names[m.predict(new_flowers)])

# 5. Flat list causes an error, double brackets fix it
# model.predict([5.1, 3.5, 1.4, 0.2])    # ValueError: Expected 2D array, got 1D array instead
print(model.predict([[5.1, 3.5, 1.4, 0.2]]))   # [0]
