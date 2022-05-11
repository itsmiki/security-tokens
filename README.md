# Security Tokens

The aim of the project is to create a program designed to generate tokens in a form of files with an appropriate extension to support the creation of phishing campaigns in companies, and which by their specificity will enable detection and localization of an attacker who broke into the system. The tokens can be for example a link or a file (docx, odt, ods, etc.). Their aim will be to inform about opening of a potentially malicious link or document, which will allow to estimate employees' awareness of such problems in case of phishing campaigns or to detect a current attack on the system along with the approximate location and permissions of the attacker.

The implementation is based on sending HTTP requests via generated tokens to a server controlled by us. When a token is used by a user, relevant information about the user will be sent to us. Each token will be equipped with a unique value based on which it will be identified in our system.

The solution currently existing on the market, which was the inspiration to create this project does not offer a client version, which would allow you to customize it to your needs and use it without intermediary in the process by software manufacturers, which ensures full confidentiality. Additionally, our solution has a wider range of token types.
