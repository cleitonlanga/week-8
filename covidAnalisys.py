# Part 1: Load and Explore Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load metadata.csv (must be in same folder or provide full path)
df = pd.read_csv(
    "metadata.csv",
    low_memory=False,
    on_bad_lines="skip",
    quoting=3,
    engine="python"
)

print("Shape of dataset:", df.shape)


# Explore
print("Shape of dataset:", df.shape)
print(df.info())
print(df.isnull().sum().sort_values(ascending=False).head(20))
print(df.describe())

# Preview
print(df.head())

# Part 2: Data Cleaning & Preparation

# Handle missing values - drop rows without publication date or title
df = df.dropna(subset=["publish_time", "title"])

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract publication year
df["year"] = df["publish_time"].dt.year

# Create abstract word count column
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

# Cleaned dataset ready
print(df[["title", "year", "abstract_word_count"]].head())

# Part 3: Analysis & Visualization

# 1. Count publications per year
year_counts = df["year"].value_counts().sort_index()
plt.figure(figsize=(10,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.xticks(rotation=45)
plt.show()

# 2. Top journals
top_journals = df["journal"].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(y=top_journals.index, x=top_journals.values, orient="h")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of Publications")
plt.show()

# 3. Most frequent words in titles
titles = " ".join(df["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()

# 4. Distribution by source
source_counts = df["source_x"].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(y=source_counts.index, x=source_counts.values, orient="h")
plt.title("Distribution of Papers by Source")
plt.xlabel("Number of Papers")
plt.show()
