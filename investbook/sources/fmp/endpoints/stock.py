from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from investbook.sources.fmp.base import FMPQueryManager


class Stock(BaseModel):
    exchange: Optional[str]
    exchangeShortName: Optional[str]
    name: Optional[str]
    price: Optional[float]
    symbol: Optional[str]
    type: Optional[str]
    
class Stock_Info(BaseModel):
    symbol: str
    exchangeShortName: Optional[str] = None  
    type: Optional[str] = None  
    name: Optional[str] = None
    price: Optional[float] = None
    changesPercentage: Optional[float] = None
    dayLow: Optional[float] = None
    dayHigh: Optional[float] = None
    yearHigh: Optional[float] = None
    yearLow: Optional[float] = None
    marketCap: Optional[int] = None
    priceAvg50: Optional[float] = None
    priceAvg200: Optional[float] = None
    volume: Optional[int] = None
    timestamp: Optional[int] = None

class Stock_News(BaseModel):
    symbol: str
    date: datetime
    title: str
    text: str
    
class StockFundamentals(BaseModel):
    symbol: str
    company_name: Optional[str]
    sector: Optional[str]
    industry: Optional[str]
    market_cap: Optional[int]
    current_price: Optional[float]
    previous_close: Optional[float]
    dividend_yield: Optional[float]
    full_time_employees: Optional[int]
    website: Optional[str]
    country: Optional[str]
    total_revenue: Optional[float]
    net_income: Optional[float]
    return_on_assets: Optional[float]
    return_on_equity: Optional[float]
    debt_to_equity: Optional[float]
    quick_ratio: Optional[float]
    current_ratio: Optional[float]



class FmpStock(FMPQueryManager):
        
    def list(self, type: str='stock') -> list[Stock]:
        """
        https://site.financialmodelingprep.com/developer/docs#symbol-list-stock-list

        Ticker stock companies
        -
        Devuelve una lista de los tickers, el exchange y el nombre de las empresas


        Returns
        -
            list of Stock
        """
        
        return [Stock.model_validate(r) for r in self.get(f'/api/v3/{type}/list')]
    
    def info(self, ticker: str) -> list[Stock_Info]: 
        """
        https://site.financialmodelingprep.com/developer/docs#full-quote-quote

        Company names 
        -
        Devuelve información de mercado de la empresa
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries

        """
        return [Stock_Info.model_validate(r) for r in self.get(f'/api/v3/quote/{ticker}')]
    
    def news(self, ticker: str) -> list[Stock_News]: 
        """
        https://site.financialmodelingprep.com/developer/docs#full-quote-quote

        Company names 
        -
        Devuelve información de mercado de la empresa
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries

        """
        return [Stock_News.model_validate(r) for r in self.get(f'/api/v3/press-releases/{ticker}')]
    
    def fundamentals(self, ticker: str) -> StockFundamentals:
        """
        Devuelve información fundamental detallada de una acción.

        Incluye: ratios, métricas clave, información de perfil y cotización.

        Docs:
        - https://site.financialmodelingprep.com/developer/docs#company-profile
        - https://site.financialmodelingprep.com/developer/docs#ratios-ttm
        - https://site.financialmodelingprep.com/developer/docs#key-metrics-ttm
        - https://site.financialmodelingprep.com/developer/docs#income-statement

        """
        profile = self.get(f"/api/v3/profile/{ticker}")[0]
        ratios = self.get(f"/api/v3/ratios-ttm/{ticker}")[0]
        # metrics = self.get(f"/api/v3/key-metrics-ttm/{ticker}")[0]
        income = self.get(f"/api/v3/income-statement/{ticker}", params={"limit": 1})[0]
        quote = self.get(f"/api/v3/quote/{ticker}")[0]

        return StockFundamentals(
            symbol=ticker,
            company_name=profile.get("companyName"),
            sector=profile.get("sector"),
            industry=profile.get("industry"),
            market_cap=quote.get("marketCap"),
            current_price=quote.get("price"),
            previous_close=quote.get("previousClose"),
            dividend_yield=(profile.get("lastDiv") or 0.0) / quote.get("price") if quote.get("price") else 0.0,
            full_time_employees=profile.get("fullTimeEmployees"),
            website=profile.get("website"),
            country=profile.get("country"),
            total_revenue=income.get("revenue"),
            net_income=income.get("netIncome"),
            return_on_assets=ratios.get("returnOnAssetsTTM"),
            return_on_equity=ratios.get("returnOnEquityTTM"),
            debt_to_equity=ratios.get("debtEquityRatioTTM"),
            quick_ratio=ratios.get("quickRatioTTM"),
            current_ratio=ratios.get("currentRatioTTM"),
        )


    
    
