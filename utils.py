import pickle
import csv
from datetime import datetime


def load_embeddings(filepath):
    """
    Loads the embeddings database from a pickle file.

    Parameters:
        filepath (str): Path to the embeddings database file.

    Returns:
        dict: The embeddings database with names as keys and embeddings as values.
    """
    with open(filepath, 'rb') as f:
        return pickle.load(f)


def save_embeddings(filepath, embeddings_db):
    """
    Saves the embeddings database to a pickle file.

    Parameters:
        filepath (str): Path to save the embeddings database.
        embeddings_db (dict): The embeddings database.
    """
    with open(filepath, 'wb') as f:
        pickle.dump(embeddings_db, f)


def log_attendance(name, log_file="results/attendance_log.csv"):
    """
    Logs attendance with the name and current timestamp to a CSV file.

    Parameters:
        name (str): Name of the recognized individual.
        log_file (str): Path to the attendance log file.
    """
    if name == "Unknown":
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, timestamp])


def read_attendance(log_file="results/attendance_log.csv"):
    """
    Reads the attendance log and prints its contents.

    Parameters:
        log_file (str): Path to the attendance log file.
    """
    try:
        with open(log_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            print("Attendance Log:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Attendance log file not found at {log_file}.")


if __name__ == "__main__":
    # Example usage of utility functions

    # Load embeddings
    embeddings = load_embeddings("data/data.pkl")
    print("Loaded embeddings:", embeddings)

    # Log attendance
    log_attendance("John Doe")

    # Read and display attendance log
    read_attendance()
