import qrcode
import os
from token_class import Token
from session_class import Session

class QR_Code(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, description, message)
        self.text = None
        self.img_path = None
        self.img = None

    def create_qrcode_token(self, ip, token_id, port = None):
        if not os.path.exists("qr_codes"):
            os.mkdir('qr_codes')

        if port == None:
            text_url = 'http://' + ip + '/token/qrcode?id=' + token_id
        else:
            text_url = 'http://' + ip + ':' + port + '/token/qrcode?id=' + token_id
        
        qrcode_img = qrcode.make(text_url)
        qrcode_img.save('qr_codes/qr_code_' + token_id + '.png')

        self.text_url = text_url
        self.img_path = os.path.abspath(os.getcwd()) + '/qr_codes'
        self.img = qrcode_img

        return
        



if __name__ == "__main__":
    test_session = Session('sesja_1')
    print(test_session.session_id)
    print(test_session.logs_path)
    


    qrcode_test1 = QR_Code(test_session, "QR_Code1")
    qrcode_test1.create_qrcode_token('145.123.45.123', qrcode_test1.token_id, "3000")
    print(qrcode_test1.text)
    print(qrcode_test1.img_path)
    qrcode_test1.img.save('qr_codes/qr_code_test' + '.png')

    qrcode_test2 = QR_Code(test_session, "QR_Code1")
    qrcode_test2.create_qrcode_token('145.123.45.123', qrcode_test2.token_id, "3000")




    # test_token1 = Token(test_session, "token1")
    # test_token2 = Token(test_session, "token2")
    #print(test_token1.token_id)

    test_session.update_session_info()