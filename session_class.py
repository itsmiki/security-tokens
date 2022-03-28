import os
import time
import hashlib

class Session():
    def __init__(self, name: str) -> None:
        self.name = name
        self.session_id = self.generate_session_id()
        self.logs_path = self.create_logs_file()
        self.info_path = self.create_session_info_file()
        
        self.session_logs = {
            "session_id": self.session_id,
            "name": self.name,
            "logs_path": self.logs_path,
            # "info_path": self.info_path,
            "tokens": []
        }
 
        self.generated_tokens = []

    def generate_session_id(self) -> bool:
        epoch = bytes(int(time.time()))     
        return hashlib.md5(epoch).hexdigest()[:16]  #troche dlugo liczy

    def create_logs_file(self) -> bool:
        if not os.path.exists("session_logs"):
            os.mkdir('session_logs')

        # with open("session_logs/" + str(self.session_id) + '.txt', 'w') as file:
        #     file.write('Create a new text file!')
        
        return os.path.abspath(os.getcwd()) + '/session_logs'

    def create_session_info_file(self) -> bool:
        if not os.path.exists("sessions"):
            os.mkdir('sessions')

        with open("sessions/" + str(self.session_id) + '.txt', 'w') as file:
            pass
        
        return os.path.abspath(os.getcwd()) + '/session_logs'

    def update_session_info(self):
        if not len(self.session_logs["tokens"]) == len(self.generated_tokens):
            for token in self.generated_tokens:
                if token.token_id not in [d["token_id"] for d in self.session_logs["tokens"]]:
                    self.session_logs["tokens"].append({
                        "token_id": token.token_id,
                        "name": token.name,
                        "description": token.description,
                        "message": token.message,
                        "logs_path": token.logs_path,

                    })

        with open("sessions/" + str(self.session_id) + '.txt', 'w', encoding='utf-8') as file:
            file.write(str(self.session_logs))

if __name__ == "__main__":
    test_session = Session("sesja_1")
    print(test_session.session_id)

    print(test_session.logs_path)