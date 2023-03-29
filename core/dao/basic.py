from core.soap import SEIClient

def set_client(func):

    client = SEIClient()
    def wraped(*args, **kwargs):
        
        return func(client, *args, **kwargs)

    return wraped

@set_client
def lst_unidades(client)->list:

    return client('listar_unidades', id_tipo_procedimento=None, id_serie=None)

@set_client
def lst_tipos_processo(client)->list:

    return client('listar_tipos_procedimento', id_unidade=None, id_serie=None)

#tipo de documento? sei é muito confuso
@set_client
def lst_tipos_documento(client)->list:

    return client('listar_series', id_unidade=None, id_tipo_procedimento=None)





