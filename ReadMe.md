Overview:
This program encrypts or decrypts a message or file and outputs it to a text file. 

Encryption

Description:
The program accepts a message or file and encrypts it with either a supplied key or generates a new key. 
The output is generated in a new file. 
The key used to encrypt the file can be exported to a file to allow for later decryption.

Parameters:

-message        The plain text message to encrypt

-file           Path to a file to be encrypted

-key            Encryption key (optional, will be generated if not provided)

-key_output     File to save the encryption key (optional)

-output         File to save the encrypted output

Example Syntax:

python C:\Code\encrpytdecrypt\endecrpyt.py encrypt -message "Hello, World!" -output encrypted_message.txt -key_output key.txt


Decryption

Description:
The program accepts a text file with an encrypted message and an encryption key.
The output is generated in a new text file.

Parameters:

-file         Path to the encrypted file

-key          Decryption key

-output       File to save the decrypted output

Example Syntax:

python C:\Code\encrpytdecrypt\endecrpyt.py decrypt -file encrypted_message.txt -key $(cat key.txt) -output decrypted_message.txt