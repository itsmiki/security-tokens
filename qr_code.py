import qrcode
import os

class QR_Code:
    def __init__(self, text, path, img):
        self.text = text
        self.path = path
        self.img = img

    def create_qrcode_token(ip, session_id, port = None):
        if not os.path.exists("qr_codes"):
            os.mkdir('qr_codes')

        if port == None:
            text_url = 'http://' + ip + '/token/qrcode?id=' + session_id
        else:
            text_url = 'http://' + ip + ':' + port + '/token/qrcode?id=' + session_id
        
        qrcode_img = qrcode.make(text_url)
        qrcode_img.save('qr_codes/qr_code_' + session_id + '.png')

        return QR_Code(text_url, os.path.abspath(os.getcwd()) + '/qr_codes', qrcode_img)
        



if __name__ == "__main__":
    qrcode_test = QR_Code.create_qrcode_token('145.123.45.123', '38j1s89j21js18', "3000")
    print(qrcode_test.text)
    print(qrcode_test.path)
    qrcode_test.img.save('qr_codes/qr_code_test' + '.png')