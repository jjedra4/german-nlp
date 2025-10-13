# German Corpora NLP Analysis

This project performs Natural Language Processing (NLP) analysis on a 1-million-sentence German text corpus from the University of Leipzig.

The primary goal is to analyze word frequencies, explore word co-occurrence relationships, and investigate linguistic patterns like Zipf's Law.

## What's Been Done

*   **Data Ingestion**: A script automatically downloads and extracts the German corpus.
*   **Word Frequency Count**: The corpus has been processed using spaCy to tokenize, lemmatize, and count the frequency of each word, filtering out stop words and punctuation.
*   **Results Saved**: The resulting word counts have been saved to a CSV file (`data/word_counts.csv`).

## Setup and Usage

Follow these steps to set up and run the project.

### 1. Create the Conda Environment

This project uses a Conda environment to manage its dependencies. The required packages are listed in the `environment.yml` file.

To create and activate the environment, run the following commands:

```bash
# Create the environment from the yml file
conda env create -f environment.yml

# Activate the new environment
conda activate nlp
```

### 2. Download the Data

The corpus data is not stored in this repository. A Python script is provided to download and extract it automatically.

Run the following command from the project root directory:

```bash
python scripts/download_data.py
```
This will download the `deu_mixed-typical_2011_1M.tar.gz` file into the `data/` directory and extract the `deu_mixed-typical_2011_1M-sentences.txt` file needed for the analysis.

### 3. Run the Analysis

The main analysis is performed in the Jupyter Notebook.

1.  Make sure your `nlp` conda environment is active.
2.  Open the `notebooks/corpora.ipynb` notebook in VS Code or your preferred Jupyter environment.
3.  You can run the cells to see the analysis that has been performed so far and continue building on it.
