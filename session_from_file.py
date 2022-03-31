import pickle

def import_session_from_file(file_location):
    with open(file_location, 'rb') as file:
        session = pickle.load(file)

    session_id = session.session_id
    
    return session
    
    
