# Security Tokens
## Overview 
Application generates tokens in a form of files with an appropriate extension to support the creation of phishing campaigns in, and which by their specificity will enable detection and localization of an attacker who broke into the system. The tokens can be for example a link or a file (docx, odt, ods, etc.). Their aim is to inform about opening of a potentially malicious link or document, which will allow to estimate employees' awareness of such problems in case of phishing campaigns or to detect a current attack on the system along with the approximate location and permissions of the attacker. 
The implementation is based on sending HTTP requests via generated tokens to a controlled server. When a token is used by a user, relevant information about the user will be sent directly to the server. Each token is equipped with a unique value based on which it will be identified in our system.

## How to use
Application can be run with Python3 (https://github.com/itsmiki/Security-Tokens/tree/main) or on Windows System directly (https://github.com/itsmiki/Security-Tokens/tree/exe).
1. Create or Load Session `Session Management` tab. Session allows a number of tokens to be grouped together, this can be useful when running a large phishing campaign. In addition, a session can be loaded even when the application is closed, and allows the tokens and all the information associated with them to be saved.
2. Create a token of your choice and describe it. The available formats are:
	* URL link
	* QR Code
	* Microsoft Word Document
	* Microsoft Excel Document
	* Open Document Calc
	* Open Document Writer
	* Shell script
	* Batch File
	
Token is a file that when opened will execute a request at the target server. All tokens assigned to the session can be seen in `Token Management` tab.

3. In `Server Management` tab turn on the server on desired ip and port (it should match the session info or localhost to which requests are forwarded).
4. Send tokens to selected users or place them in a suitable location in the system.
5. When token is used (file is opened or executed) request will be sent to the server, all the notifications can be seen in `Message Center` tab.

##
The project was carried out as part of the Telephoners research club at the AGH University of Science.
