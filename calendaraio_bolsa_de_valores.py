import pandas_market_calendars as mcal

calendario = mcal.get_calendar("BMF")
print(calendario)
dias_negociacao_2024 = calendario.schedule(start_date="2024-01-01",end_date="2024-12-31")

print(dias_negociacao_2024)