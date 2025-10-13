import os
import requests
from tqdm import tqdm
import tarfile
import sys

# --- Configuration ---
# Direct URL for the 1M mixed-typical sentences corpus from 2011
DATA_URL = "https://downloads.wortschatz-leipzig.de/corpora/deu_mixed-typical_2011_1M.tar.gz"
# Relative path to save the data
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
FILE_NAME = "deu_mixed-typical_2011_1M.tar.gz"
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)
EXTRACTION_DIR = "deu_mixed-typical_2011_1M"
EXTRACTED_FILE_NAME = "deu_mixed-typical_2011_1M-sentences.txt"
EXTRACTED_FILE_PATH = os.path.join(DATA_DIR, EXTRACTION_DIR, EXTRACTED_FILE_NAME)

def main():
    """
    Main function to download and extract the corpus data.
    """
    # --- Ensure data directory exists ---
    os.makedirs(DATA_DIR, exist_ok=True)

    # --- Download the data if it doesn't exist ---
    if not os.path.exists(FILE_PATH):
        print(f"'{FILE_NAME}' not found. Downloading from {DATA_URL}...")
        try:
            response = requests.get(DATA_URL, stream=True)
            response.raise_for_status()  # Raise an exception for bad status codes

            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte

            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
            with open(FILE_PATH, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()

            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print("ERROR, something went wrong during download.")
                sys.exit(1) # Exit with an error code
            else:
                print(f"Successfully downloaded and saved to '{FILE_PATH}'")

        except requests.exceptions.RequestException as e:
            print(f"Error downloading the file: {e}")
            sys.exit(1) # Exit with an error code
    else:
        print(f"Found '{FILE_NAME}' at '{FILE_PATH}'.")

    # --- Extract the data if it hasn't been extracted ---
    if not os.path.exists(EXTRACTED_FILE_PATH):
        print(f"Extracting '{FILE_NAME}'...")
        try:
            # Use "r:gz" to open gzipped tar files
            with tarfile.open(FILE_PATH, "r:gz") as tar:
                print(f"Extracting all files.")
                tar.extractall(path=DATA_DIR)
                print(f"Extraction complete. Please check the '{DATA_DIR}/{EXTRACTION_DIR}' for the sentences file.")

        except tarfile.TarError as e:
            print(f"Error extracting the tar file: {e}")
            sys.exit(1) # Exit with an error code
    else:
        print(f"Found extracted file '{EXTRACTED_FILE_PATH}'.")

if __name__ == "__main__":
    main()
