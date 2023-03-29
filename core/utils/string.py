

def letra_minuscula_comeco(txt:str)->str:
    if txt[0].isupper():
        txt = txt[0].lower()+txt[1:]
    return txt

def letra_maiuscula_comeco(txt:str)->str:
    if txt[0].islower():
        txt = txt[0].upper()+txt[1:]
    return txt

def camel_case(txt:str, inicio_minuscula=True)->str:

    if inicio_minuscula:
        txt = letra_minuscula_comeco(txt)
    else:
        txt = letra_maiuscula_comeco(txt)
    if "_" in txt:
        splited = txt.split('_')
        new_text=[]
        for i, item in enumerate(splited):
            if i > 0:
                item = letra_maiuscula_comeco(item)
            new_text.append(item)
        txt = ''.join(new_text)
    return txt

    


    