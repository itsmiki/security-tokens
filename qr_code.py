import qrcode
import os
from token_class import Token
from session_class import Session
from token_types_class import tokenTypes

class QR_Code(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, tokenTypes.QR_CODE, description, message)
        self.text_url = None
        self.img_path = None

    def create_token(self, ip, port = None):
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/qr_codes"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/qr_codes')

        if port == None:
            text_url = 'http://' + ip + '/token/qrcode?id=' + self.token_id
        else:
            text_url = 'http://' + ip + ':' + port + '/token/qrcode?id=' + self.token_id
        
        qrcode_img = qrcode.make(text_url)
        qrcode_img.save(os.path.dirname(os.path.abspath(__file__)) + '/qr_codes/qr_code_' + self.token_id + '.png')

        self.text_url = text_url
        self.img_path = os.path.dirname(os.path.abspath(__file__)) + '/qr_codes'

        return
    

        



if __name__ == "__main__":
    test_session = Session('sesja_1')
    # print(test_session.session_id)
    # print(test_session.logs_path)
    # test_session.generated_tokens[0].text_url
    
    

    qrcode_test1 = QR_Code(test_session, "QR_Code1")
    qrcode_test1.create_token('145.123.45.123', "3000")
    # print(qrcode_test1.text_url)
    # print(qrcode_test1.img_path)

    qrcode_test2 = QR_Code(test_session, "QR_Code1")
    qrcode_test2.create_token('145.123.45.123', "3000")

    test_session.save_session_info()


    #sesja = Session('SESJA')

