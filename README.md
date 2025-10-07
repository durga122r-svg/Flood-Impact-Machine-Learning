# Predicting Flood-Induced Damage on Concrete Structures using Machine Learning

## 📘 Project Overview

This project uses **Machine Learning (Random Forest Classifier)** to predict the potential **damage level** (Low, Medium, or High) on concrete structures caused by flooding. It simulates a dataset representing real-world parameters such as flood depth, duration, concrete grade, soil type, and structure age.

The model can help engineers and planners assess **structural vulnerability** and prioritize **maintenance or reinforcement** measures after floods.

---

## 🚀 Features

* Synthetic dataset generation for flood and structure parameters.
* Data preprocessing and categorical encoding.
* Random Forest-based damage prediction.
* Model evaluation with accuracy, confusion matrix, and classification report.
* Visualization of feature importance.
* Exports trained model and dataset for reuse.

---

## 🧠 Technologies Used

* **Python 3.x**
* **Pandas**, **NumPy** – data handling
* **Matplotlib**, **Seaborn** – data visualization
* **Scikit-learn** – model training and evaluation
* **Joblib** – model serialization

---

## 📂 Project Structure

```
Flood-Damage-ML-Project/
│
├── Flood_Damage_ML_Project.ipynb   # Main Jupyter Notebook
├── flood_damage_dataset.csv         # Generated dataset
├── flood_damage_model.pkl           # Saved ML model
└── README.md                        # Project documentation
```

---

## 🧩 How It Works

1. **Data Generation**: Randomly simulates parameters like flood depth, duration, concrete grade, etc.
2. **Label Creation**: Combines features to derive a logical `Damage_Level` label.
3. **Model Training**: Trains a Random Forest Classifier.
4. **Evaluation**: Prints accuracy, confusion matrix, and classification report.
5. **Visualization**: Displays feature importance.

---

## 📊 Sample Output

**Accuracy:** ~85–95% (varies with random data)

**Most influential features:**

* Flood Depth (m)
* Duration of Submersion (days)
* Structure Age (yrs)

---

## ⚙️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/Flood-Damage-ML-Project.git
   ```
2. Navigate into the project folder:

   ```bash
   cd Flood-Damage-ML-Project
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the notebook:

   ```bash
   jupyter notebook Flood_Damage_ML_Project.ipynb
   ```

---

## 📈 Future Improvements

* Replace synthetic data with real flood and structural datasets.
* Implement regression to estimate **repair cost** instead of categorical damage levels.
* Deploy as a **web app** using Streamlit or Flask.

---

## 🏗️ Author

Developed by **Chandra Sekhar** — B.Tech Civil Engineering (NIT Manipur)

*For academic demonstration and research purposes only.*
