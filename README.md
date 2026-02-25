🎓 Student Performance Analysis & Dashboard
📌 Project Overview

This project focuses on analyzing student academic performance using data analysis and visualization techniques. It includes data preprocessing, outlier detection, categorical encoding, correlation analysis, and an interactive dashboard built with Streamlit.

The main objective is to understand the factors affecting students' final exam marks and visualize key insights.

📂 Dataset Information

The dataset contains student-related information such as:

Study Hours

Attendance Percentage

Gender

Internet Access

Extracurricular Activities

Family Income

Final Exam Marks (Target Variable)

⚙️ Technologies Used

Python 🐍

Pandas

NumPy

Matplotlib

Seaborn

Streamlit

🔎 Project Workflow
1️⃣ Data Loading

Dataset loaded using Pandas.

Checked shape, info, and summary statistics.

2️⃣ Data Cleaning

Checked for missing values.

Checked for duplicate values.

No missing or duplicate values found.

3️⃣ Outlier Detection & Removal

Used IQR (Interquartile Range) method.

Removed outlier from final_exam_marks.

Verified removal using boxplot.

4️⃣ Encoding Categorical Variables

Applied One Hot Encoding for nominal variables:

Gender

Internet Access

Extracurricular Activities

Applied Ordinal Encoding for:

Family Income (Low < Medium < High)

5️⃣ Correlation Analysis

Generated correlation heatmap.

Identified relationship between study hours and final marks.

6️⃣ Data Visualization

Distribution of final marks.

Study Hours vs Final Marks (Scatter Plot)

Attendance vs Final Marks

Gender vs Final Marks

Family Income vs Final Marks

📊 Streamlit Dashboard Features

The project includes an interactive dashboard with:

📌 Key Performance Indicators:

Total Students

Average Marks

Highest Marks

🔎 Sidebar Filters:

Study Hours Range Filter

📈 Visualizations:

Scatter Plot (Study Hours vs Marks)

Histogram (Marks Distribution)

Correlation Heatmap

💡 Insights Section:

Highlights relationship between study hours and performance.

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
