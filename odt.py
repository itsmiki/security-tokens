import os
import zipfile
import fileinput
import shutil

from token_class import Token
from session_class import Session
from token_types_class import tokenTypes

class ODT(Token):
    def __init__(self, session: Session, name: str, description: str = None, message: str = None):
        super().__init__(session, name, tokenTypes.ODT, description, message)
        self.odt_path = None

    def create_token(self, ip, port = None):
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/odt"):
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + '/odt')

        if port == None:
            replacement = "http://" + ip + "/token?id=" + self.token_id
        else:
            replacement = "http://" + ip + ":" + port + "/token?id=" + self.token_id

        token = "http://my-server-ip-address"


        tmpDirURL = os.path.dirname(os.path.abspath(__file__)) + "/templates/~odt_contents"
        zipSourceFileURL = os.path.dirname(os.path.abspath(__file__)) + "/templates" + "/" + "template.odt"
        zipOutFileURL = os.path.dirname(os.path.abspath(__file__)) + '/odt/' + self.token_id + ".odt"
        xmlFileURL = tmpDirURL + "/" + "content.xml"
        #
        # Unzip ODT
        #
        zipdata = zipfile.ZipFile(zipSourceFileURL)
        zipdata.extractall(tmpDirURL)
        #
        # Adding token with replace
        #
        for line in fileinput.input(xmlFileURL, inplace=1):
            print(line.replace(token, replacement))
        # Zip contents of the temporary directory to ODT
        # Use file list from the original archive
        # This preserves the file structure in the new Zip file

        with zipfile.ZipFile(zipOutFileURL, 'w') as outzip:
            zipinfos = zipdata.infolist()
            for zipinfo in zipinfos:
                fileName = zipinfo.filename # The name and path as stored in the archive
                fileURL = tmpDirURL + "/" + fileName # The actual name and path
                outzip.write(fileURL, fileName)

        shutil.rmtree(os.path.dirname(os.path.abspath(__file__)) + "/templates/~odt_contents")


if __name__ == "__main__":
    
    sesja1 = Session("testsesja")
    tokentest = ODT(sesja1, "test")
    
    tokentest.create_token("127.0.0.1", "5000")
