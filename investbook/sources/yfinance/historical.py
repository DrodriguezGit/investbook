from typing import List
from pydantic import BaseModel
import yfinance as yf
import pandas as pd

class StockHistoricalData(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    dividends: float
    stock_splits: float
    
    

class YahooFinanceHistorical:
    
    def get_historical_data(self, stock_ticker: str, period: str = "max") -> List[StockHistoricalData]:
        """
        Consulta el historial de precios de una acción.

        Params
        -
        :param stock_ticker (str): Ticker de la acción (Ej. 'AAPL' para Apple)
        :param period (str): Periodo del historial (Ej. 'max', '1y', '5d')

        Returns
        -
        List[StockHistoricalData]: Lista con los datos históricos de la acción.
        """
        stock = yf.Ticker(stock_ticker)
        historical_data = stock.history(period=period)

        # Convertir el DataFrame a una lista de objetos StockHistoricalData
        historical_objects = []
        for date, row in historical_data.iterrows():
            historical_objects.append(StockHistoricalData(
                date=date.strftime('%Y-%m-%d'),  # Convertir la fecha a formato string
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume'],
                dividends=row['Dividends'],
                stock_splits=row['Stock Splits']
            ))

        return historical_objects
