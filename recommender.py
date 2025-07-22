import pandas as pd

def get_colleges_for_career(career, csv_path="college_data.csv"):
    """
    Returns a DataFrame of colleges related to the given career from the CSV.
    
    Parameters:
    - career (str): Career name to filter colleges.
    - csv_path (str): Path to the college data CSV file.

    Returns:
    - DataFrame containing college info for the given career.
    """
    df = pd.read_csv(csv_path)
    return df[df["career"] == career]

def get_top_careers(career_scores, top_n=3):
    """
    Sorts and returns the top N careers from the score dictionary.

    Parameters:
    - career_scores (dict): Dictionary of career -> score
    - top_n (int): Number of top careers to return

    Returns:
    - List of tuples (career, score)
    """
    sorted_scores = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:top_n]
