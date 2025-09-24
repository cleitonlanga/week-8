CORD-19 Data Explorer

A simple data science workflow project using the CORD-19 dataset
.
This project loads the metadata.csv file, cleans and analyzes the data, generates visualizations, and provides an interactive Streamlit app for exploration.

🚀 Features

Data Loading & Cleaning

Handles missing and corrupted rows

Extracts publication years

Adds abstract word count column

Exploratory Data Analysis

Publications count per year

Top journals publishing COVID-19 research

Word cloud of paper titles

Distribution of papers by source

Interactive Streamlit App

Year range slider filter

Displays sample data

Interactive charts and word cloud

📂 Project Structure
week-8/
│── app.py              # Streamlit application
│── analysis.ipynb      # Jupyter notebook for data exploration (optional)
│── metadata.csv        # CORD-19 dataset metadata (must be downloaded separately)
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

⚙️ Installation
1. Clone the repository
git clone: https://github.com/cleitonlanga/week-8.git

2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

📊 Usage
Run the Jupyter Notebook
jupyter notebook analysis.ipynb

Run the Streamlit App
streamlit run app.py


If streamlit is not recognized, use:

python -m streamlit run app.py

⚠️ Notes

The file metadata.csv is large (~800k rows) and may contain corrupted rows.
The code uses:

pd.read_csv("metadata.csv", engine="python", on_bad_lines="skip", quoting=3)


to skip problematic lines safely.

Only a few rows are skipped; analysis is not affected.

