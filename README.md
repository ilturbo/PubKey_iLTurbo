# PubKey iLTurbo
This script allows you to easily convert from a compressed public key (Secp256k1) to an uncompressed public key (Secp256k1).
On the forums of cryptographers and programmers, I saw a lot of questions and requests for this conversion. People are wondering that there are many scripts for generating public keys in a compressed form.
Yes, the compressed public key is convenient and secure according to cryptographers.
My professional duty made me create this script.
Get an uncompressed public key in one click and enjoy the process!

# Installation:

Create a list of compressed public keys to file: PubKey_02compressed.txt

git clone https://github.com/ilturbo/PubKey_iLTurbo.git

cd PubKey_iLTurbo

sudo apt install python3

chmod +x PubKey_iLTurbo.py

./PubKey_iLTurbo.py

Enjoy the process!

The result of the uncompressed public keys will be saved to the file: PubKey_04uncompressed.txt
