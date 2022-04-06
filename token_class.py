from session_class import Session
import os
import time

from session_from_file import import_session_from_file
from token_types_class import tokenTypes

class Token():
    def __init__(self, session: Session, name: str, token_type: tokenTypes, description: str = None, message: str = None):
        self.name = name
        self.token_type = token_type.name
        self.description = description
        self.message = message
        self.token_id = str(session.session_id) + str(len(session.generated_tokens))
        self.logs_path = self.create_logs_file(session.session_id)

        session.generated_tokens.append(self)

    def create_logs_file(self, session_id) -> bool:
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/session_logs/" + session_id):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "/session_logs/" + session_id)

        with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + session_id + "/" + str(self.token_id) + '.txt', 'w') as file:
            pass
        
        return os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + session_id + "/" + self.token_id + ".txt"

    def add_connection_log(self, ip, time_epoch, user_agent):
        log = {
            "token_id": self.token_id,
            "ip": ip,
            "time_epoch": time_epoch,
            "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_epoch)),
            "user-agent": user_agent,
        }

        with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + self.token_id[:16] + "/" + str(self.token_id) + '.txt', 'a') as file:
            file.write(str(log) + "\n")
        


        
if __name__ == "__main__":
    # test_session = Session('sesja_1')
    # print(test_session.session_id)
    # #print(test_session.logs_path)

    # test_token1 = Token(test_session, "token1")
    # test_token2 = Token(test_session, "token2")
    # #print(test_token1.token_id)
    # test_token1.add_connection_log('192.168.0.1', time.time(), {"s": "asdas"})
    # test_token1.add_connection_log('192.168.0.2', time.time(), {"s": "asdas"})
    # test_token1.add_connection_log('192.168.0.3', time.time(), {"s": "asdas"})
    # test_session.save_session_info()

    # del test_session

    test_session_from_file = import_session_from_file(r"C:\Users\Admin\Documents\SEMESTR 6\KOŁO NAUKOWE\sessions\0aed8ec9e00390b3.pkl")

    print(test_session_from_file.session_id)
    test_token1 = test_session_from_file.generated_tokens[0]
    test_token1.add_connection_log('192.168.0.3', time.time(), {"s": "asdas"})
    #print(test_session_from_file)

    print(test_session_from_file.get_token_names())