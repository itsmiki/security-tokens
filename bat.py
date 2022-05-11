from token_class import Token
from session_class import Session
from token_types_class import tokenTypes

import os
import stat

class BAT(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, tokenTypes.BAT, description, message)
        self.path = None

    def create_token(self, ip, port = None) -> str:
        if port == None:
            s = 'curl http://' + ip + '/token?id=' + self.token_id
        else:
            s = 'curl http://' + ip  + ':' + port + '/token?id=' + self.token_id

        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/bat"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/bat')


        filename = (os.path.dirname(os.path.abspath(__file__)) + '/bat/' + self.token_id + '.bat')
        self.path = (os.path.dirname(os.path.abspath(__file__)) + '/bat/' + self.token_id + '.bat')
        file = open(filename, "w")
        file.write(s)
        file.close() 
        st = os.stat(filename)
        os.chmod(filename, st.st_mode | stat.S_IEXEC)



if __name__ == "__main__":
    test_session = Session('sesja_1')
    # print(test_session.session_id)
    # print(test_session.logs_path)
    # test_session.generated_tokens[0].text_url
    
    

    qrcode_test1 = BAT(test_session, "BAT1")
    qrcode_test1.create_token('127.0.0.1', "5000")
    # print(qrcode_test1.text_url)
    # print(qrcode_test1.img_path)

    qrcode_test2 = BAT(test_session, "BAT2")
    qrcode_test2.create_token('192.168.0.101', "5000")

    test_session.save_session_info()


    #sesja = Session('SESJA')


        