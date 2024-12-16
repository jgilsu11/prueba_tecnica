
import pandas as pd
import numpy as np
import requests
import os
import sys

pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

import psycopg2
from psycopg2 import sql

def crear_id(df_anti,nombre_col_antigua,nombre_col_nueva,nombre_col_id_nuevo):
    anio= pd.DataFrame()
    anio[nombre_col_nueva]=df_anti[nombre_col_antigua].unique()
    anio.index=anio.index+1
    df_nuevo=anio.reset_index().rename(columns={'index': nombre_col_id_nuevo})
    return df_nuevo