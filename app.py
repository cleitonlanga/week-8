import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (metadata.csv)")


@st.cache_data
@st.cache_data
@st.cache_data
def load_data():
    df = pd.read_csv(
        "metadata.csv",
        on_bad_lines="skip",  # skip bad rows
        engine="python",  # tolerant parser
        quoting=3,  # ignore quotation marks
    )
    df = df.dropna(subset=["publish_time", "title"])
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    df["abstract_word_count"] = (
        df["abstract"].fillna("").apply(lambda x: len(x.split()))
    )
    return df


df = load_data()

# Sidebar filters
year_range = st.slider(
    "Select year range", int(df["year"].min()), int(df["year"].max()), (2020, 2021)
)
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

st.subheader("Sample Data")
st.write(filtered.head())

# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(y=top_journals.index, x=top_journals.values, orient="h", ax=ax)
ax.set_title("Top Journals")
ax.set_xlabel("Number of Publications")
st.pyplot(fig)

# Word Cloud
st.subheader("Word Cloud of Titles")
titles = " ".join(filtered["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
