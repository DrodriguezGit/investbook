from pydantic import BaseModel
from investbook.sources.fmp.base import FMPQueryManager

class Logo(BaseModel):
    image: bytes

    def save(self, path: str):
        with open(path, 'wb') as file:
            file.write(self.image)


class FmpCompany(FMPQueryManager):
    
    def get_logo(self, img_name: str):
        """
        
        https://site.financialmodelingprep.com/developer/docs#company-logo
 
        Company logo
        
        Descarga el logo de una compañía como imagen PNG y lo guarda donde le pidas
        
        Params
        -
        :param logo (str): Nombre del logo a buscar (e.g., 'EURUSD.png').
        :param save_path (str): Ruta donde se guardará la imagen. Si no se proporciona, retornará el contenido binario.
        
        Returns
        -
        Si `save_path` está definido, guarda la imagen en el disco y retorna la ruta. 
        De lo contrario, retorna el contenido binario de la imagen.
        """
        response = self.get(f'image-stock/{img_name}', as_dict=False)

        return Logo(image=response.content)

       
    def get_profile(self, ticker: str):
        """
        https://site.financialmodelingprep.com/developer/docs#company-profile-company-information


        Profile companies
        -
        Devuelve una lista con toda la información básica del ticker 
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries
        """
        return self.get(f'/api/v3/profile/{ticker}')
    
    

    # Endpoint de pago
    # def stock_peers(self, symbol: str):
    #     return self.get('v4/stock_peers', symbol=symbol)
    