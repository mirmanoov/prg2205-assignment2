import json

def load_user_data(file_path='user_data.json'):
    """Load user data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"name": "Player", "level": 1, "score": 0}

def save_user_data(user_data, file_path='user_data.json'):
    """Save or update user data to a JSON file."""
    try:
        with open(file_path, 'r') as file:
            all_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_data = {}

    # Update existing user's data or add a new user
    all_data[user_data['username']] = user_data

    with open(file_path, 'w') as file:
        json.dump(all_data, file, indent=4)

