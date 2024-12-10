from __future__ import annotations
from investbook.sources.finhub.base import FinHubQueryManager
from typing import List, Optional
from pydantic import BaseModel

class SymbolSearch(BaseModel):
    description: str  
    displaySymbol: str  
    symbol: str  
    type: str  

class AnalystTrend(BaseModel):
    buy: int  
    hold: int  
    sell: int  
    period: str  

class MarketStatus(BaseModel):
    exchange: str 
    holiday: Optional[str] 
    isOpen: bool  
    session: str  
    timezone: str  
    t: int  
    
class CompanyProfile(BaseModel):
    country: str  
    currency: str  
    exchange: str  
    ipo: str  
    marketCapitalization: float  
    name: str  
    phone: str  
    shareOutstanding: float  
    ticker: str  
    weburl: str  
    logo: str  
    finnhubIndustry: str
    


class FinHubInfo(FinHubQueryManager):
        
    def get_symbol(self, q: str) -> List[SymbolSearch]:
        """
        https://finnhub.io/docs/api/symbol-search
        
        -
        Busca los símbolos que mejor se ajusten a su consulta.
    
        :param query (str): Nombre de empresa 
        
        
        return: Devuelve una lista de empresas 
        """
        response = self.get('/search', q=q)

        # Extraer la lista de resultados del campo "result"
        result_data = response.get("result", [])

        return [SymbolSearch.model_validate(r) for r in result_data]
    
    def get_trends(self, symbol: str) -> List[AnalystTrend]:
        """
        https://finnhub.io/docs/api/recommendation-trends

        -
        Obtener las tendencias de las recomendaciones de analistas para un ticker.
        
        :param symbol (str): El símbolo de la acción (ej. 'AAPL' para Apple)
        
        return: Tendencias de recomendaciones de los analistas para el símbolo
        """
        return [AnalystTrend.model_validate(r) for r in self.get('/stock/recommendation', symbol=symbol)]
    
    def get_status(self, exchange: str) -> MarketStatus:
        """
        https://finnhub.io/docs/api/market-status
    
        -
        Obtiene la situación actual del mercado que busques
        
        :param exchange (str): El mercado en cuestión que busques
        
        return: Devuelve una lista con información del mercado con datos como si están en vacaciones, está abierto o no y qué momento de la sesión está
       
        """
        return MarketStatus.model_validate(self.get('/stock/market-status', exchange=exchange))

    def company_profile(self, symbol: str):
        """
        https://finnhub.io/docs/api/company-profile2
        
        -
        Obtiene la información general del ticker buscado
        
        :param symbol (str): ticker de la empresa
        
        return: Devuelve un diccionario con todo tipo de información (country, currency, name, ticker...)  
        
        """    
        return CompanyProfile.model_validate(self.get('stock/profile2', symbol=symbol))
    
    