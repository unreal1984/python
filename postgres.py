import pandas as pd
import matplotlib.pyplot as plt
import  sqlalchemy 

# PostgreSQL
conn = sqlalchemy.create_engine('postgresql://scott:tiger@172.16.250.142:5432/scottiger',connect_args={'options': '-csearch_path={}'.format('distrib')})
df = pd.read_sql_table("d_product", con=conn)
print(df)