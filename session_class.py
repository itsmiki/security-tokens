import os
import time
import hashlib
import pickle


class Session():
    # Klasa sesja agreguje podległe po nią tokeny
    # w momencie stworzenia instancji sesja tworzone są foldery do logów i informacji na jej temat
    def __init__(self, name: str) -> None:
        self.name = name
        self.session_id = self.generate_session_id()
        self.logs_path = self.create_logs_file()
        self.info_path = self.create_session_info_file()
        
        self.session_logs = {
            "session_id": self.session_id,
            "name": self.name,
            "logs_path": self.logs_path,
            "info_path": self.info_path,
            "tokens": []
        }
 
        self.generated_tokens = [] #lista tokenów należących do sesji


    # generowanie id dla sesji
    def generate_session_id(self) -> bool:
        epoch = bytes(int(time.time()))     
        return hashlib.md5(epoch).hexdigest()[:16]  #troche dlugo liczy


    # tworzymy folder /session_logs do logów na temat zapytań z tokenów
    def create_logs_file(self) -> bool:
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/session_logs"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/session_logs')

        return os.path.dirname(os.path.abspath(__file__)) + '/session_logs'


    # tworzymy folder /sessions w którym będzie zapisywana sesja z jej tokenami, aby był do niej dostęp po zamknięciu programu
    def create_session_info_file(self) -> bool:
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/sessions"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/sessions')

        with open(os.path.dirname(os.path.abspath(__file__)) + "/sessions/" + str(self.session_id) + '.pkl', 'w') as file:
            pass
        
        return os.path.dirname(os.path.abspath(__file__)) + '/session_logs'

    
    # zapisywanie sesji do pliku
    def save_session_info(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + "/sessions/" + str(self.session_id) + '.pkl', 'wb') as file:
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)

    
    # zwraca listę z nazwami tokenów, gdzie miejsce nazwy na liście odpowiada miejscu tokena na liście self.generated_tokens
    def get_token_names(self) -> list:
        token_names_list = []
        for token in self.generated_tokens:
            token_names_list.append(token.name)
        
        return token_names_list

        


if __name__ == "__main__":
    test_session = Session("sesja_1")
    print(test_session.session_id)

    print(test_session.logs_path)