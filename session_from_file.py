import pickle

def import_session_from_file(file_location):
    with open(file_location, 'rb') as file:
        session = pickle.load(file)

    #session_id = session.generated_tokens[0].name
    #print(session_id)
    return session
    
    
