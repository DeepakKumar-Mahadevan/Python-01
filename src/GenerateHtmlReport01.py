import pandas as pd

pd.set_option('display.width', 1000)
pd.set_option('colheader_justify', 'center')

# df = pd.read_csv(r'E:\Chicago_E_Drive\Deepak DOCs\Study\Data Analytics\Sample_Data\ManUtdPlayers.csv',encoding='latin-1')
df = pd.read_excel(r'E:\Chicago_E_Drive\Deepak DOCs\Study\Data Analytics\Sample_Data\ManUtdPlayers.xlsx')
# print(df)

# 1. Set up multiple variables to store the titles, text within the report
page_title_text='My report'
title_text = 'Manchester United Players'
text = 'Hello, This is a Report of all Man Utd Players.'
List_Header = 'List of Man Utd Players'

# 2. Combine them together using a long f-string
html = f'''
    <html>
        <head>
            <title>{page_title_text}</title>
        </head>
        <link rel="stylesheet" type="text/css" href="df_style.css"/>
        <body>
            <h1>{title_text}</h1>
            <p>{text}</p>
            <h2>{List_Header}</h2>
            {df.to_html(classes='mystyle')}
        </body>
    </html>
    '''
# 3. Write the html string as an HTML file
with open('html_report01.html', 'w') as f:
    f.write(html)
