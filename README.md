# 🎓 Student Performance Analysis & Interactive Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a student performance dataset and builds an **interactive Streamlit dashboard** to visualize key academic insights.

The goal is to analyze factors affecting students' **Final Exam Marks** and present meaningful insights through data visualization and filtering.

---

## 📂 Dataset Description

The dataset includes the following features:

- 📚 Study Hours  
- 🏫 Attendance Percentage  
- 👩‍🎓 Gender  
- 🌐 Internet Access  
- 🎯 Extracurricular Activities  
- 💰 Family Income  
- 📝 Final Exam Marks *(Target Variable)*  

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Streamlit**

---

## 🔎 Project Workflow

### 1️⃣ Data Loading
- Loaded dataset using Pandas
- Checked dataset shape and structure
- Analyzed summary statistics

### 2️⃣ Data Cleaning
- Checked for missing values
- Checked for duplicate values
- Confirmed dataset integrity

### 3️⃣ Outlier Detection & Removal
- Used **IQR (Interquartile Range)** method
- Removed outlier from `final_exam_marks`
- Verified using boxplots

### 4️⃣ Encoding Categorical Variables
- **One-Hot Encoding** for:
  - Gender
  - Internet Access
  - Extracurricular Activities

- **Ordinal Encoding** for:
  - Family Income (Low < Medium < High)

### 5️⃣ Correlation Analysis
- Generated correlation heatmap
- Identified strong positive relationship between:
  - Study Hours
  - Final Exam Marks

### 6️⃣ Data Visualization
- Distribution of Final Marks
- Study Hours vs Final Marks (Scatter Plot)
- Attendance vs Final Marks
- Gender vs Final Marks
- Family Income vs Final Marks

---

## 📊 Interactive Streamlit Dashboard

The project includes a dynamic dashboard with:

### ✅ Key Performance Indicators
- Total Students
- Average Marks
- Highest Marks

### 🔎 Sidebar Filter
- Study Hours Range Slider

### 📈 Visualizations
- Scatter Plot (Study Hours vs Marks)
- Histogram (Marks Distribution)
- Correlation Heatmap

### 💡 Insights Section
- Highlights performance trends
- Shows correlation impact

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

🚀 How to Run the Project
Step 1: Install Required Libraries
pip install pandas numpy matplotlib seaborn streamlit
Step 2: Run the Streamlit App
streamlit run your_script_name.py
🎯 Key Insights

Students who study more hours tend to score higher.

Positive correlation between study hours and final exam marks.

Family income shows some influence on performance.

Marks distribution is moderately spread.

📁 Project Structure
Student-Performance-Analysis/
│
├── student_dataset.csv
├── student_analysis.py
├── student_dashboard.py
└── README.md
📌 Future Improvements

Add Machine Learning model for marks prediction.

Deploy dashboard online.

Add more interactive filters.

Improve UI design.

👩‍💻 Author

Muskan Saini
AIML Student
