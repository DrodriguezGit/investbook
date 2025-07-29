from pydantic import BaseModel
from typing import Optional, List
from investbook.sources.fmp.base import FMPQueryManager

class Historical(BaseModel):

    symbol: str
    date: str  # Usamos 'date' en vez de 'from'
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[int]




class FmpHistorical(FMPQueryManager):
    
    def historical(self, ticker: str, interval: str = "4hour", limit: int =365) -> List[Historical]:
        """
        Consulta precios históricos intradía del activo con un intervalo fijo.

        Endpoint:
        https://site.financialmodelingprep.com/developer/docs#stock-price-change-quote

        Parámetros
        ----------
        ticker : str
            Símbolo del activo (por ejemplo: 'AAPL').
        interval : str, opcional
            Intervalo de tiempo entre datos (por defecto '4hour').
            Opciones válidas: '1min', '5min', '15min', '30min', '1hour', '4hour'.

        Devuelve
        --------
        List[Historical]
            Lista con los últimos n registros de precios del activo, incluyendo:
            fecha, apertura, máximo, mínimo, cierre, volumen y símbolo.

        """
        data = self.get(f"api/v3/historical-chart/{interval}/{ticker}")[:limit]
        
        validated = []
        for entry in data:
            entry["symbol"] = ticker  # esto garantiza que Pydantic no falle
            validated.append(Historical.model_validate(entry))

        return validated
    
    
    