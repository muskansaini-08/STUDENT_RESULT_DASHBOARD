#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[14]:

df = pd.read_csv("student_dataset.csv")
df.head()


# In[12]:


df.shape  # check the dimensions of your DataFrame.


# In[4]:


df.info()
# df.info() shows us that there are 4 objects that are needed to converted categorical to numerical


# In[6]:


df.describe()


# # CHECK FOR MISSING VALUES

# In[7]:


# To check missing values
df.isnull().sum()


# In[50]:


# There are no missing values in the dataset


# # CHECK FOR DUPLICATES VALUES

# In[10]:


# To check duplicates 
duplicates = df.duplicated() 
print(duplicates)


# No duplicates is present in the dataset

# Our target variable is final_exam_marks.

# # OUTLIER DETECTION AND REMOVAL

# In[20]:


import seaborn as sns              # Import Seaborn for statistical data visualization
import matplotlib.pyplot as plt    # Import Matplotlib for plotting and figure control

# Select only numeric columns (int64 and float64 types) from the DataFrame
numeric_cols = df.select_dtypes(include=['int64','float64']).columns

# Create a new figure with a specific size (15 inches wide, 8 inches tall)
plt.figure(figsize=(15,8))

# Loop through each numeric column with its index
for i, col in enumerate(numeric_cols):
    # Create a subplot in a 3x3 grid, placing the plot in position i+1
    plt.subplot(3,3,i+1)
    
    # Draw a boxplot for the current numeric column
    sns.boxplot(y=df[col])
    
    # Set the title of the subplot to the column name
    plt.title(col)

# Adjust layout so plots and titles don’t overlap
plt.tight_layout()

# Display the final figure with all boxplots
plt.show()


#   One Outlier is present in the final_exam_marks so we remove it.

# In[21]:


import pandas as pd

# Let's assume 'final_exam_marks' is the column with outliers
Q1 = df['final_exam_marks'].quantile(0.25)   # First quartile (25th percentile)
Q3 = df['final_exam_marks'].quantile(0.75)   # Third quartile (75th percentile)
IQR = Q3 - Q1                                # Interquartile Range

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out rows that are outside the bounds
df_no_outliers = df[(df['final_exam_marks'] >= lower_bound) & (df['final_exam_marks'] <= upper_bound)]

print("Original shape:", df.shape)
print("After removing outliers:", df_no_outliers.shape)


# In[23]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(y=df_no_outliers['final_exam_marks'])
plt.title("Final Exam Marks (After Outlier Removal)")
plt.show()
# THIS SHOWS OUTLIER IS REMOVED.


# In[26]:


# ENCODE CATEGORICAL VARIABLE(CONVERTING CATEGORICAL TO NUMERICAL.)
df.select_dtypes(include=['object']).columns


# In[28]:


# Loop through each categorical (object type) column
# Print the column name and its unique values
# This helps us understand whether the column is nominal (unordered categories)
# or ordinal (ordered categories) based on the unique values
for col in df.select_dtypes(include=['object']).columns:
    print(col)                 # print column name
    print(df[col].unique())    # print unique values in that column
    print("-------------")     # separator for readability


# How to know if its nominal.
# 
# If the unique values are just labels with no natural order
# 
# (e.g., Male/Female, Yes/No, Sports/Music), then the column is NOMINAL.
# 
# If the unique values have a meaningful order or ranking # (e.g., Low < Medium < High, Grade A > Grade B > Grade C), then it's ORDINAL.

# In[30]:


# For nominal we use One Hot Encoding
df = pd.get_dummies(df, columns=['gender','internet_access','extracurricular'], drop_first=True)


# In[31]:


# Define a mapping dictionary for ordinal categories
# 'Low' < 'Medium' < 'High' → we assign increasing numeric values
income_mapping = {'Low': 0, 'Medium': 1, 'High': 2}

# Apply the mapping to the 'family_income' column
# This replaces text categories with their corresponding numeric codes
df['family_income'] = df['family_income'].map(income_mapping)


# In[32]:


df.info()


#  There are no object (categorical) columns left in the DataFrame.
#  
#  This means all categorical variables have been successfully encoded into numerical form.

# # COORELATION MATRICS.

# In[33]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()


# # distribution of targe variable

# In[34]:


sns.histplot(df['final_exam_marks'], kde=True)
plt.show()


# # Study Hours vs Final Marks

# In[ ]:


sns.scatterplot(x=df['study_hours'], y=df['final_exam_marks'])
plt.show()


# # Attendance vs Final Marks

# In[36]:


sns.scatterplot(x=df['attendance_percentage'], y=df['final_exam_marks'])
plt.show()


# # Gender vs Final Marks

# In[40]:


sns.boxplot(x=df['gender_Male'], y=df['final_exam_marks'])
plt.show()


# # Family Income vs Final Marks

# In[41]:


sns.boxplot(x=df['family_income'], y=df['final_exam_marks'])
plt.show()


# # SIMPLE STUDENT DASHBOARD

# In[51]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Student Performance Analysis Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

# ===============================
# Sidebar Filters
# ===============================
st.sidebar.header("🔎 Filter Options")

min_hours = int(df['study_hours'].min())
max_hours = int(df['study_hours'].max())

selected_hours = st.sidebar.slider(
    "Select Study Hours Range",
    min_value=min_hours,
    max_value=max_hours,
    value=(min_hours, max_hours)
)

filtered_df = df[(df['study_hours'] >= selected_hours[0]) & 
                 (df['study_hours'] <= selected_hours[1])]

# ===============================
# Key Metrics Section
# ===============================
st.subheader("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(filtered_df))
col2.metric("Average Marks", round(filtered_df['final_exam_marks'].mean(), 2))
col3.metric("Highest Marks", filtered_df['final_exam_marks'].max())

st.markdown("---")

# ===============================
# Dataset Preview
# ===============================
with st.expander("📂 View Dataset"):
    st.dataframe(filtered_df)

# ===============================
# Visualizations Section
# ===============================
st.subheader("📈 Visual Analysis")

col1, col2 = st.columns(2)

# Scatter Plot
with col1:
    st.markdown("### Study Hours vs Final Marks")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(x=filtered_df['study_hours'], 
                    y=filtered_df['final_exam_marks'], 
                    hue=filtered_df['final_exam_marks'],
                    palette="viridis",
                    ax=ax1)
    st.pyplot(fig1)

# Histogram
with col2:
    st.markdown("### Distribution of Final Marks")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_df['final_exam_marks'], 
                 kde=True, 
                 color='skyblue',
                 ax=ax2)
    st.pyplot(fig2)

st.markdown("---")

# ===============================
# Correlation Heatmap
# ===============================
st.subheader("🔗 Correlation Heatmap")

fig3, ax3 = plt.subplots(figsize=(8,5))
sns.heatmap(filtered_df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm",
            ax=ax3)
st.pyplot(fig3)

st.markdown("---")

# ===============================
# Insights Section
# ===============================
st.subheader("💡 Key Insights")

st.success("""
• Students who study more hours tend to score higher marks.  
• There is a positive correlation between study hours and final exam marks.  
• Marks distribution appears moderately spread with few high performers.  
""")

st.markdown("<center>🚀 Built with Streamlit</center>", unsafe_allow_html=True)


# In[46]:


import os

# Current working directory (where your script is running)
current_path = os.getcwd()
print("Current folder path:", current_path)


# In[53]:





# In[ ]:





# In[ ]:




