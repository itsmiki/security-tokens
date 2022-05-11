from distutils.log import info
import json
from session_class import Session
import os
import time

from session_from_file import import_session_from_file
from token_types_class import tokenTypes

class Token():
    # klasa token zawiera podstawowe informacje o konkretnym tokenie
    # nie jest ona wywoływana bezpośrednio, a jest jedynie klasą którą dziedziczą klasy poszczególnych tokenów
    # każdy token jest podległy jednej sesji o id równym szesnastu pierwszym znakom id tokenu


    def __init__(self, session: Session, name: str, token_type: tokenTypes, description: str = None, message: str = None):
        self.name = name
        self.token_type = token_type.name
        self.description = description
        self.message = message
        self.token_id = str(session.session_id) + str(len(session.generated_tokens))
        self.logs_path = self.create_logs_file(session.session_id)
        #token w mwmencie stworzenia dodany jest do listy tokenów sesji do której należy
        session.generated_tokens.append(self)


    # tworzymy folder z logami na temat tokenu w folderze session_logs tworząc ścieżkę session_logs/[id_sesji]/[id_tokenu].txt
    def create_logs_file(self, session_id) -> bool:
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/session_logs/" + session_id):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "/session_logs/" + session_id)

        with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + session_id + "/" + str(self.token_id) + '.txt', 'w') as file:
            pass
        
        with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + session_id + "/" + str(self.token_id) + '_info.txt', 'w', encoding='utf-8') as file:
            info = {
                "token_name": self.name,
                "token_type": self.token_type,
                "description": self.description,
                "message": self.message,
            }
            file.write(str(info) + "\n")

        return os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + session_id + "/" + self.token_id + ".txt"

    # do pliku stworzonego w poprzedniej funkcji dodajemy kolejne linijki za każdym razem jak token zostanie użyty
    def add_connection_log(self, ip, time_epoch, user_agent):
        log = {
            "token_id": self.token_id,
            "token_name": self.name,
            "token_type": self.token_type,
            "description": self.description,
            "message": self.message,
            "ip": ip,
            "time_epoch": time_epoch,
            "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_epoch)),
            "user-agent": user_agent,
        }

        with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + self.token_id[:16] + "/" + str(self.token_id) + '.txt', 'a', encoding="utf-8") as file:
            file.write(str(log) + "\n")

    def get_token_logs(self) -> list:
        list_of_logs = []
        with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + self.token_id[:16] + "/" + str(self.token_id) + '.txt', 'r') as file:
            for line in file:
                list_of_logs.append(json.loads(line.replace("\'", "\"")))
        return list_of_logs
        


        
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

    test_session_from_file = import_session_from_file(r"C:\Users\Admin\Documents\SEMESTR 6\KOLO_NAUKOWE\GUI 2\sessions\7654681d4e618cca.pkl")

    #print(test_session_from_file.session_id)
    test_token1 = test_session_from_file.generated_tokens[0]
    test_token1.add_connection_log('192.168.0.3', time.time(), {"s": "asdas"})
    #print(test_session_from_file)
    test_session_from_file.generated_tokens[0].get_token_logs()

    #print(test_session_from_file.get_token_names())