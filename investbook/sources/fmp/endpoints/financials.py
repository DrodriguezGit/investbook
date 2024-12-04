from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

from investbook.sources.fmp.base import FMPQueryManager

class Statement(BaseModel):
    acceptedDate: Optional[str]
    calendarYear: Optional[str]
    cik: Optional[str]
    costAndExpenses: Optional[float]
    costOfRevenue: Optional[float]
    date: Optional[str]
    depreciationAndAmortization: Optional[float]
    ebitda: Optional[float]
    ebitdaratio: Optional[float]
    eps: Optional[float]
    epsdiluted: Optional[float]
    fillingDate: Optional[str]
    finalLink: Optional[str]
    generalAndAdministrativeExpenses: Optional[float]
    grossProfit: Optional[float]
    grossProfitRatio: Optional[float]
    incomeBeforeTax: Optional[float]
    incomeBeforeTaxRatio: Optional[float]
    incomeTaxExpense: Optional[float]
    interestExpense: Optional[float]
    interestIncome: Optional[float]
    link: Optional[str]
    netIncome: Optional[float]
    netIncomeRatio: Optional[float]
    operatingExpenses: Optional[float]
    operatingIncome: Optional[float]
    operatingIncomeRatio: Optional[float]
    otherExpenses: Optional[float]
    period: Optional[str]
    reportedCurrency: Optional[str]
    researchAndDevelopmentExpenses: Optional[float]
    revenue: Optional[float]
    sellingAndMarketingExpenses: Optional[float]
    sellingGeneralAndAdministrativeExpenses: Optional[float]
    symbol: Optional[str]
    totalOtherIncomeExpensesNet: Optional[float]
    weightedAverageShsOut: Optional[float]
    weightedAverageShsOutDil: Optional[float]
    

class FmpFinancialStates(FMPQueryManager):
    
    def income_statement(self, ticker: str, period: str) -> list[Statement]:
        """
        https://site.financialmodelingprep.com/developer/docs#income-statements-financial-statements    
     
        Income statement 
        -
        Devuelve una lista con el acceso en tiempo real a los datos de la cuenta de resultados de una amplia gama de empresas
        
        Params
        -
         :param ticker (str)
         :param period (str): annual | quarter

        Returns
        -
            list of dictionaries

        """
        return [Statement.model_validate(r) for r in self.get(f'/api/v3/income-statement/{ticker}', period=period)]    