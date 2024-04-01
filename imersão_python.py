# -*- coding: utf-8 -*-
"""Imersão Python


AULA 02 - IMPORTAÇÃO
"""

import pandas as pd

df_principal = pd.read_excel("/content/acoes_pura.xlsx", sheet_name="Principal")
df_principal.head(10)

df_total_acoes = pd.read_excel("/content/acoes_pura.xlsx", sheet_name="Total_de_acoes")
df_total_acoes

df_ticker = pd.read_excel("/content/acoes_pura.xlsx", sheet_name="Ticker")
df_ticker