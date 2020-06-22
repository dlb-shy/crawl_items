import base64

from Crypto.Cipher import AES


def get_params( page):
    '''
    "{"rid":"A_PL_0_4930102132","offset":"20","total":"false","limit":"20","csrf_token":""}"
    :param page:
    :return:
    '''
    iv = "0102030405060708"
    first_key = "0CoJUm6Qyw8W8jud"
    second_key = 'F' * 16
    if page == 0:
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
    else:
        offset = str((page - 1) * 20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'false') # rid可以选择添加
    encText = AES_encrypt(first_param, first_key, iv)
    encText = AES_encrypt(encText.decode('utf-8'), second_key, iv)
    return encText


def AES_encrypt(text, key, iv):
    # AES加密
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypt_text = encryptor.encrypt(text.encode('utf-8'))
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text