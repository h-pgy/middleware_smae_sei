


def s_n_to_bool(val:str)->bool:

    val = str(val).lower().strip()
    if val == 's':
        return True
    elif val == 'n':
        return False
    else:
        raise ValueError(f'Unexpected S/N val: {val}')