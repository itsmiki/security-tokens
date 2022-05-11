import os
import shutil
import zipfile
from zipfile import ZipFile
from PIL import Image

from token_class import Token
from session_class import Session
from token_types_class import tokenTypes

class MSEXCEL(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, tokenTypes.EXCEL, description, message)
        self.path = None
    
    #From unpacked xlsx making new xlsx with replaced strings
    def create_xlsx(self, path, ziph):
        for root, dirs, files in os.walk(path):
            for file1 in files:
                ziph.write(os.path.join(root, file1), os.path.relpath(os.path.join(root, file1), os.path.join(path,'')))
        ziph.close()

    #Creating image with for identifing curent token
    def create_image(self): 
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/msexcel_images"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/msexcel_images')
        img = Image.new("RGB", (1, 1))
        img.save(os.path.dirname(os.path.abspath(__file__)) + "/msexcel_images/" + self.token_id + ".png", "PNG")

    def create_token(self, ip, port):
        self.create_image()

        #Using template file and extracting to "temp" folder
        with ZipFile(os.path.dirname(os.path.abspath(__file__)) + "/templates/template.xlsx") as template:
            template.extractall(path= os.path.dirname(os.path.abspath(__file__)) + "/templates/temp")
        
        #Replacing string
        replacetoken = "http://" + ip + ":" + port + "/token?id=" + self.token_id
        with open(os.path.dirname(os.path.abspath(__file__)) + "/templates/temp/xl/drawings/_rels/drawing1.xml.rels", "r+") as footer:
            content = footer.read().replace("HONEYDROP_TOKEN_URL", replacetoken)
            footer.seek(0)
            footer.write(content)
            footer.truncate()
        
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/msexcel"):
                os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "/msexcel")

        #Making new xlsx with done token
        with zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__)) + "/msexcel/" + self.token_id + ".xlsx", "w", zipfile.ZIP_DEFLATED) as zipf:
            self.create_xlsx(os.path.dirname(os.path.abspath(__file__)) + '/templates/temp/', zipf)

        self.path = os.path.dirname(os.path.abspath(__file__)) + "/msexcel/" + self.token_id + ".xlsx"

        shutil.rmtree(os.path.dirname(os.path.abspath(__file__)) + "/templates/temp")


if __name__ == "__main__":
    
    sesja2 = Session("testsesja2", "127.0.0.1", "8080")
    tokentest2 = MSEXCEL(sesja2, "test2")
    tokentest2.create_token("127.0.0.1", "8080")