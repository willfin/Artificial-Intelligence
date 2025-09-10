
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")  # Download from Kaggle and keep in working dir
print(df.shape)
df.head()

X = df.drop("target", axis=1)  # Features
y = df["target"]               # Target (1 = disease, 0 = no disease)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

rf_clf = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42
)
rf_clf.fit(X_train, y_train)

y_pred = rf_clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["No Disease", "Disease"],
            yticklabels=["No Disease", "Disease"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Heart Disease")
plt.show()

feature_importances = pd.Series(rf_clf.feature_importances_, index=X.columns)
feature_importances.sort_values().plot(kind="barh", figsize=(8,5))
plt.title("Feature Importances (Heart Disease)")
plt.show()