import hashlib
# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
#print("welcome python hashlib world!")
# 256
def hashMe(a):
    hash_256 = hashlib.sha256()
    hash_str = a
    hash_256.update(hash_str.encode('utf-8'))
    hash_256_value = hash_256.hexdigest()
    obj = hashlib.new('ripemd160', hash_256_value.encode('utf-8'))
    ripemd_160_value = obj.hexdigest()
    #print("sha256:", hash_256_value)  # 16进制
    return ripemd_160_value
