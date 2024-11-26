from investbook.sources.fmp.base import FMPQueryManager
    
class FmpCompanyLogo(FMPQueryManager):
    
    def company_logo(self, logo: str, save_path: str = None):
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
        endpoint = f'image-stock/{logo}'
            # Genera la URL completa
        url = self.url_maker(self.base_url, endpoint)
        response = self.session.get(url, headers=self.headers, stream=True)
        response.raise_for_status()  # Levanta excepción si el estado HTTP es un error
            
        if save_path:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            return save_path
            
            # Retorna el contenido binario si no se especificó `save_path`
        return response.content


    #Endpoint de pago
    # def stock_peers(self, symbol: str):
    #     return self.get('v4/stock_peers', symbol=symbol)