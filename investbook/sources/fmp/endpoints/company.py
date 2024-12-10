from __future__ import annotations
from pydantic import BaseModel
from typing import Optional
from investbook.sources.fmp.base import FMPQueryManager

class Logo(BaseModel):
    image: bytes

    def save(self, path: str):
        with open(path, 'wb') as file:
            file.write(self.image)
            
class Profile(BaseModel):
    address: Optional[str]
    beta: Optional[float]
    ceo: Optional[str]
    changes: Optional[float]
    cik: Optional[str]
    city: Optional[str]
    companyName: Optional[str]
    country: Optional[str]
    currency: Optional[str]
    cusip: Optional[str]
    dcf: Optional[float]
    dcfDiff: Optional[float]
    defaultImage: Optional[bool]
    description: Optional[str]
    exchange: Optional[str]
    exchangeShortName: Optional[str]
    fullTimeEmployees: Optional[str]
    image: Optional[str]
    industry: Optional[str]
    ipoDate: Optional[str]
    isActivelyTrading: Optional[bool]
    isAdr: Optional[bool]
    isEtf: Optional[bool]
    isFund: Optional[bool]
    isin: Optional[str]
    lastDiv: Optional[float]
    mktCap: Optional[int]
    phone: Optional[str]
    price: Optional[float]
    sector: Optional[str]
    state: Optional[str]
    symbol: Optional[str]
    volAvg: Optional[int]
    website: Optional[str]
    zip: Optional[str]


class FmpCompany(FMPQueryManager):
    
    def get_logo(self, img_name: str) -> list[Logo]:
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

       
    def get_profile(self, ticker: str) -> list[Profile]:
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
        return [Profile.model_validate(r) for r in self.get(f'/api/v3/profile/{ticker}')]    