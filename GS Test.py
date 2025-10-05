import Glassdoor_Scraper as gs
import pandas as pd

# author: Bashar

df = gs.get_jobs('data scientist',1000, False, 9, None, 25, 'glassdoor_jobs', True)
print(df.head())