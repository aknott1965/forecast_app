# utils.py

import pyodbc
from .models import ActualSales

def import_sales_data():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=libsql16;'
        'DATABASE=Budget;'
        'UID=djangoapps;'
        'PWD=nfcGYEnPJs89Rm3HJDr6GoQzGBK&NP;'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.[Actual Sales]')
    rows = cursor.fetchall()

    for row in rows:
        ActualSales.objects.get_or_create(
            Sales_person=row.Sales_person,
            Cust_no=row.Cust_no,
            Sales_Amount=row.Sales_Amount,
            # Assign values for other fields
        )

    conn.close()
