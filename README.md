# 🎓 Student Performance Analysis & Interactive Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Deployed](https://img.shields.io/badge/Deployment-Live-success)

---

## 🚀 Live Deployment

🌐 **Live Streamlit App:**  
👉 https://student-result-dashboard.streamlit.app/

This project has been successfully deployed using **Streamlit Cloud**, allowing users to interact with the dashboard in real time.

---

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a student performance dataset and builds an **interactive Streamlit dashboard** to visualize academic insights.

The objective is to analyze the factors affecting students' **Final Exam Marks** and present meaningful trends through interactive visualizations and filtering mechanisms.

---

## 🎯 Problem Statement

Understanding the factors that influence student academic performance helps in:

- Identifying key performance drivers
- Improving study strategies
- Supporting data-driven academic decisions

This project explores how variables such as study hours, attendance, family income, and extracurricular activities impact final exam performance.

---

## 📂 Dataset Features

The dataset contains the following attributes:

- 📚 **Study Hours**
- 🏫 **Attendance Percentage**
- 👩‍🎓 **Gender**
- 🌐 **Internet Access**
- 🎯 **Extracurricular Activities**
- 💰 **Family Income**
- 📝 **Final Exam Marks** *(Target Variable)*

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
- Generated summary statistics

### 2️⃣ Data Cleaning
- Identified missing values
- Checked for duplicate records
- Ensured dataset consistency

### 3️⃣ Outlier Detection & Removal
- Applied **IQR (Interquartile Range)** method
- Removed outliers from `final_exam_marks`
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

## 📊 Interactive Dashboard Features

### ✅ Key Performance Indicators (KPIs)
- Total Students
- Average Marks
- Highest Marks

### 🔎 Sidebar Filters
- Study Hours Range Slider

### 📈 Visualizations Included
- Scatter Plot (Study Hours vs Marks)
- Histogram (Marks Distribution)
- Correlation Heatmap

### 💡 Insights Section
- Highlights major performance trends
- Displays correlation findings
- Helps understand academic impact factors

---

## 🎯 Key Insights

- Students who study more hours tend to score higher.
- There is a strong positive correlation between study hours and final exam marks.
- Family income shows moderate influence on academic performance.
- Marks distribution is moderately spread across students.

---

## 🏗️ Project Structure

```
Student-Performance-Analysis/
│
├── student_dataset.csv
├── student_analysis.py
├── student_dashboard.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn streamlit
```

OR (if using requirements file):

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run student_dashboard.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 🌐 Deployment Details

- Platform Used: **Streamlit Cloud**
- Live URL: https://student-result-dashboard.streamlit.app/
- Public Access: Enabled
- Real-time interactive filtering supported

---

## 📌 Future Improvements

- Add Machine Learning model for marks prediction
- Integrate advanced statistical analysis
- Add downloadable reports
- Improve UI/UX design
- Add multi-filter comparison
- Deploy using custom domain

---

## 📈 Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Encoding Techniques
- Outlier Detection
- Correlation Analysis
- Data Visualization
- Interactive Dashboard Development
- Cloud Deployment

---

## 👩‍💻 Author

**Muskan Saini**  
B.Tech CSE (AI & ML) Student  
Passionate about Data Science & Machine Learning  

🔗 Live App: https://student-result-dashboard.streamlit.app/

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub to show support!
