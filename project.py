
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


np.random.seed(42)

n_samples = 500

data = pd.DataFrame({
    'Flood_Depth_m': np.random.uniform(0.2, 3.0, n_samples),
    'Duration_days': np.random.randint(1, 30, n_samples),  
    'Concrete_Grade': np.random.choice(['M20', 'M25', 'M30', 'M35'], n_samples),
    'Structure_Age_yrs': np.random.randint(1, 50, n_samples),
    'Soil_Type': np.random.choice(['Clay', 'Silty', 'Sandy'], n_samples),
    'Previous_Floods': np.random.randint(0, 5, n_samples)
})

data['Concrete_Grade'] = data['Concrete_Grade'].map({'M20': 20, 'M25': 25, 'M30': 30, 'M35': 35})
data['Soil_Type'] = data['Soil_Type'].map({'Clay': 0, 'Silty': 1, 'Sandy': 2})

data['Damage_Level'] = (
    (0.4*data['Flood_Depth_m']) +
    (0.03*data['Duration_days']) +
    (0.02*data['Previous_Floods']) +
    (0.015*data['Structure_Age_yrs']) -
    (0.005*data['Concrete_Grade'])
)

data['Damage_Level'] = pd.qcut(data['Damage_Level'], 3, labels=['Low', 'Medium', 'High'])

print(data.head())

X = data.drop('Damage_Level', axis=1)
y = data['Damage_Level']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues', fmt='d',
            xticklabels=['Low', 'Medium', 'High'], yticklabels=['Low', 'Medium', 'High'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(7,4))
sns.barplot(x='Importance', y='Feature', data=feature_importances, palette='viridis')
plt.title('Feature Importance')
plt.show()

data.to_csv('flood_damage_dataset.csv', index=False)
import joblib
joblib.dump(model, 'flood_damage_model.pkl')

print("\nProject completed successfully! Files saved:")
print("- flood_damage_dataset.csv")
print("- flood_damage_model.pkl")
