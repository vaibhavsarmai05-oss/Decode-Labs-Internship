from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()

X = iris.data

y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("="*41)
print("     Data Classification Using AI")
print("="*41)
print("Dataset: Iris Flower Dataset\n")
print("Possible flower types:")
for flower in iris.target_names:
    print("-", flower)


print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nActual Labels:", y_test)

print("\nPredicted Labels:", y_pred)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nEnter flower measurements:")

sepal_length = float(input("Sepal length: "))
sepal_width = float(input("Sepal width: "))
petal_length = float(input("Petal length: "))
petal_width = float(input("Petal width: "))

new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(new_flower)

print("Predicted flower type:", iris.target_names[prediction[0]])
