import os
import shutil
import zipfile
from zipfile import ZipFile
from PIL import Image

from token_class import Token
from session_class import Session
from token_types_class import tokenTypes

class MSWORD(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, tokenTypes.WORD, description, message)
        self.docx_path = None
    
    #From unpacked docx making new docx with replaced strings
    def create_docx(self, path, ziph):
        for root, dirs, files in os.walk(path):
            for file1 in files:
                ziph.write(os.path.join(root, file1), os.path.relpath(os.path.join(root, file1), os.path.join(path,'')))
        ziph.close()

    #Creating image with for identifing curent token
    def create_image(self): 
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/msword_images"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/msword_images')
        img = Image.new("RGB", (1, 1))
        img.save(os.path.dirname(os.path.abspath(__file__)) + "/msword_images/" + self.token_id + ".png", "PNG")

    def create_token(self, ip, port):
        
        self.create_image()

        replacetoken = "http://" + ip + ":" + port + "/token?id=" + self.token_id
        #replacetoken = "http://" + ip + ":" + port + "/" + self.token_id

        with ZipFile(os.path.dirname(os.path.abspath(__file__)) + "/templates/template.docx") as template:
            template.extractall(path= os.path.dirname(os.path.abspath(__file__)) + "/templates/temp")
        
        #Replacing string
        with open(os.path.dirname(os.path.abspath(__file__)) + "/templates/temp/word/_rels/footer2.xml.rels", "r+") as footer:
            content = footer.read().replace("HONEYDROP_TOKEN_URL", replacetoken)
            footer.seek(0)
            footer.write(content)
            footer.truncate()
        with open(os.path.dirname(os.path.abspath(__file__)) + "/templates/temp/word/footer2.xml", "r+") as footer:
            content = footer.read().replace("HONEYDROP_TOKEN_URL", replacetoken)
            footer.seek(0)
            footer.write(content)
            footer.truncate()
        
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/msword"):
                os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/msword')

        with zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__)) + "/msword/" + self.token_id + ".docx", "w", zipfile.ZIP_DEFLATED) as zipf:
            self.create_docx(os.path.dirname(os.path.abspath(__file__)) + '/templates/temp/', zipf)

        shutil.rmtree(os.path.dirname(os.path.abspath(__file__)) + "/templates/temp")


if __name__ == "__main__":
    
    sesja1 = Session("testsesja")
    tokentest = MSWORD(sesja1, "test")
    
    tokentest.create_token("127.0.0.1", "8080")