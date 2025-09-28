import Glassdoor_Scraper as gs
import pandas as pd

# path = "C:/Program Files/chromedriver-win64" 
df = gs.get_jobs('data scientist',15, False, 15)
print(df.head())