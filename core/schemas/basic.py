from pydantic import BaseModel, validator

from .validators import s_n_to_bool

class Unidade(BaseModel):

    id_unidade : str
    sigla : str
    descricao : str
    sin_protocolo : bool
    sin_arquivamento : bool
    sin_ouvidoria : bool

    #validators

    _protocolo_to_bool = validator('sin_protocolo', 
                                   allow_reuse=True, pre=True, always=True)(s_n_to_bool)
    _arquivamento_to_bool = validator('sin_arquivamento', 
                                      allow_reuse=True, pre=True, always=True)(s_n_to_bool)
    _ouvidoria_to_bool = validator('sin_ouvidoria', 
                                   allow_reuse=True, pre=True, always=True)(s_n_to_bool)



