import pandas as pd
import pandas_profiling
import os

data = pd.read_excel('test1.xlsx')
# data.profile_report('Titanic Dataset')
pandas_profiling.ProfileReport(data)
profile = data.profile_report(title="oil_data")
profile.to_file(output_file="oil_data.html")