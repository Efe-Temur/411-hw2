from Crypto.Cipher import Salsa20


key =  14656892184006070584

ciphertext_1 = b"Vbq\x8a\xe3\xb7Rgl-\x14\x8bNS\xeb\x01\xbd\xdf\x1f\x14\x84{\xdanX,\xa5\x98RM\x98\r\xd7\x1e\x9dO\x14\xa7\x8cX\xcb\xad\xf2\xc9\x1f\xc1]\xef\x908I\xe0\xcf\x10%.ulh\xe7\xd6\x9d<\xb9a\xda\xb0\xa2d\xe9\x18\xef9\x99ttP\x9blw\x0e\xe7\xd6\xbb1\xf4?\x16kf\x87\x19\xbe\x94O\xe8\x1d\x08\xe4\xff)\x99']\xda\x191=|H"
ciphertext_2 = b'\eda\x01q+]\x8c\x06[\xa2/\xb8\xcaX\x1f\x8f:\xc97\x0f)\xa5\x84Y\t\xdc\x07\xd2L\xb3V\x14\xad\x8bU\x99\xa3\xf2\x9dK\xc8V\xab\xdd\nS\xe9\xcf\x05$r,\t<\x9e\xd0\x9b<\xbcx\x99\xaf\xed7\xf9\x13\xff9\x88r \\\x9b}>\x1d\xeb'
ciphertext_3 = b'ea,\x14\x88NW\xbfh\xb9\xcdX\x0f\x83}\xc0cX5\xa5\x9e\x1e^\xd0\x03\xc5\x1e\xa3U@\xa1\x85H\xc0'

key = key.to_bytes(32, byteorder='big')

ctext_nonce = ciphertext_1[:8]
ciphertext = ciphertext_1 [8:]
cipher = Salsa20 .new(key, nonce = ctext_nonce)
dtext = cipher.decrypt(ciphertext)

print("decoded text: ", dtext.decode('UTF-8'))

ctext_nonce = ciphertext_1[:8]
ciphertext = ciphertext_2 [5:]
cipher = Salsa20 .new(key, nonce = ctext_nonce)
dtext = cipher.decrypt(ciphertext)

print("decoded text: ", dtext.decode('UTF-8'))

ctext_nonce = ciphertext_1[:8]
ciphertext = ciphertext_3 [1:]
cipher = Salsa20 .new(key, nonce = ctext_nonce)
dtext = cipher.decrypt(ciphertext)

print("decoded text: ", dtext.decode('UTF-8'))