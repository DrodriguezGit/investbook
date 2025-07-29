from pydantic import BaseModel
import yfinance as yf
from yahoo_fin import stock_info as si


class StockInfo(BaseModel):
    symbol: str
    company_name: str
    sector: str
    industry: str
    market_cap: int
    current_price: float
    previous_close: float
    dividend_yield: float
    full_time_employees: int
    website: str
    country: str
    total_revenue: float
    net_income: float
    return_on_assets: float
    return_on_equity: float
    debt_to_equity: float
    quick_ratio: float
    current_ratio: float

    


class YahooFinanceInfo:
    
    def get_info(self, stock_ticker: str) -> StockInfo:
        """
        Consulta la información básica de un ticker de acción.

        Params
        -
        :param stock_ticker (str): Ticker de la acción (Ej. 'AAPL' para Apple)

        Returns
        -
        StockInfo: Objeto con la información básica de la acción.
        """
        stock = yf.Ticker(stock_ticker)
        info = stock.info
        

        return StockInfo(
            symbol=stock_ticker,
            company_name=info.get('longName', 'N/A'),
            sector=info.get('sector', 'N/A'),
            industry=info.get('industry', 'N/A'),
            market_cap=info.get('marketCap', 0),
            current_price=info.get('currentPrice', 0.0),
            previous_close=info.get('previousClose', 0.0),
            dividend_yield=info.get('dividendYield', 0.0),
            full_time_employees=info.get('fullTimeEmployees', 0),
            website=info.get('website', 'N/A'),
            country=info.get('country', 'N/A'),
            total_revenue=info.get('totalRevenue', 0.0),
            net_income=info.get('netIncomeToCommon', 0.0),
            return_on_assets=info.get('returnOnAssets', 0.0),
            return_on_equity=info.get('returnOnEquity', 0.0),
            debt_to_equity=info.get('debtToEquity', 0.0),
            quick_ratio=info.get('quickRatio', 0.0),
            current_ratio=info.get('currentRatio', 0.0),
        )
        
