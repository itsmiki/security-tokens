import os
import zipfile
import fileinput
import shutil

from token_class import Token
from session_class import Session
from token_types_class import tokenTypes

class ODS(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, tokenTypes.ODS, description, message)
        self.ods_path = None

    def create_token(self, ip, port = None):
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/ods"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/ods')

            if port == None:
                replacement = "http://" + ip + "/token?id=" + self.token_id
            else:
                replacement = "http://" + ip + ":" + port + "/token?id=" + self.token_id

            token = "http://my-server-ip-address"

            tmpDirURL = os.path.dirname(os.path.abspath(__file__)) + "/templates/~ods_contents"
            zipSourceFileURL = os.path.dirname(os.path.abspath(__file__)) + "templates" + "/" + "template.ods"
            zipOutFileURL = os.path.dirname(os.path.abspath(__file__)) + '/ods/' + self.token_id + ".ods"
            xmlFileURL = tmpDirURL + "/" + "content.xml"

            zipdata = zipfile.ZipFile(zipSourceFileURL)
            zipdata.extractall(tmpDirURL)

            for line in fileinput.input(xmlFileURL, inplace=1):
                print(line.replace(token, replacement))

            with zipfile.ZipFile(zipOutFileURL, 'w') as outzip:
                zipinfos = zipdata.infolist()
                for zipinfo in zipinfos:
                    fileName = zipinfo.filename  # The name and path as stored in the archive
                    fileURL = tmpDirURL + "/" + fileName  # The actual name and path
                    outzip.write(fileURL, fileName)

            # shutil.rmtree(os.path.dirname(os.path.abspath(__file__)) + "/templates/~ods_contents")

        if __name__ == "__main__":
            sesja1 = Session("testsesja")
            tokentest = ODS(sesja1, "test")

            tokentest.create_token("127.0.0.1", "5000")

            
