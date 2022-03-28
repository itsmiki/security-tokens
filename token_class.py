from session_class import Session
import os

class Token():
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        self.name = name
        self.description = description
        self.message = message
        self.token_id = str(session.session_id) + str(len(session.generated_tokens))
        self.logs_path = self.create_logs_file(session.session_id)

        session.generated_tokens.append(self)

    def create_logs_file(self, session_id) -> bool:
        if not os.path.exists("session_logs/" + session_id):
            os.mkdir("session_logs/" + session_id)

        with open('session_logs/' + session_id + "/" + str(self.token_id) + '.txt', 'w') as file:
            pass
        
        return os.path.abspath(os.getcwd()) + '/session_logs/' + session_id + "/" + self.token_id + ".txt"






if __name__ == "__main__":
    test_session = Session('sesja_1')
    print(test_session.session_id)
    print(test_session.logs_path)

    test_token1 = Token(test_session, "token1")
    test_token2 = Token(test_session, "token2")
    #print(test_token1.token_id)

    test_session.update_session_info()
        