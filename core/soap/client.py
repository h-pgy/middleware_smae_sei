from zeep import Client
from zeep.xsd import Nil
from functools import partial
from core.utils.string import camel_case
from core.config import WSDL, USER, PASSW

from typing import Callable

class SEISoap:

    def __init__(self):

        self.client = Client(WSDL)

    def __get_service(self, service_name:str)->Callable:

        #nomes de servico sao em camel case
        service_name = camel_case(service_name)
        try:
            return getattr(self.client.service, service_name)
        except KeyError:
            raise ValueError(f'Servico {service_name} não disponível')

    def authorized_service(self, service_name:str)->Callable:

        service_func = self.__get_service(service_name)
        authorized = partial(
                            service_func, 
                            SiglaSistema=USER,
                            IdentificacaoServico=PASSW
                        )
        
        return authorized

    def __solve_null(self, val):

        if val is None:
            return Nil
        return val
    
    def __solve_params(self, kwargs:dict)->dict:

        #nos parametros eh camelcase com maiuscula no começo
        params = {
                camel_case(key, inicio_minuscula=False) : self.__solve_null(val)
                for key, val in kwargs.items()
                }

        return params

    def __call__(self, service_name:str, *_, **kwargs):

        service = self.authorized_service(service_name)

        #os parametros sao sempre title case
        
        params = self.__solve_params(kwargs)

        return service(**params)
        
    