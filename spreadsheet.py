import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

json_key_path = "stats-433808-2b0112b3a676.json"

