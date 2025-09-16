import pickle

def load_wesad_subject(file_path):
    """
    Loads the WESAD data for a single subject from a pickle file.
    
    Args:
        file_path (str): The path to the .pkl file.
        
    Returns:
        dict: The loaded data, containing signals and labels.
    """
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file, encoding='latin1')
        return data
    except FileNotFoundError:
        print(f"Error: Data file not found at {file_path}")
        return None