from config import settings
import os
from sqlalchemy import create_engine
import pandas as pd


# Utilities
def import_to_psql(excel_table_path: str):
    """Quick function to import rows from file to db"""
    engine = create_engine(settings.POSTGRES_URL, echo=False)
    df = pd.read_excel(excel_table_path)
    df.to_sql(name="item", if_exists='append', con=engine, index=False)
    print('[INFO] OK')


def add_row_to_xlsx(file_name: str, source: dict, sheet_title: str = 'Sheet1') -> None:
    """Using this function you can add one / or many (depending on DataFrame) strings to .xlsx spreadsheet.
    Also, it allows to create table with many sheets and add a row to specific sheet
    depending on which sheet name had specified."""
    df = pd.DataFrame(source)
    path = f'{settings.BASE_DIR}/data/{file_name}'
    if not os.path.exists(path):
        df.to_excel(path, sheet_name=sheet_title, index=False)
    else:
        with pd.ExcelFile(path, engine='openpyxl') as reader:
            sheet_titles = reader.sheet_names
            if sheet_title in sheet_titles:
                info = reader.parse(sheet_name=sheet_title)
                rows = len(info)
                start = rows + 1
                with pd.ExcelWriter(path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                    df.to_excel(writer, startrow=start, sheet_name=sheet_title, index=False, header=False)
            else:
                with pd.ExcelWriter(path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                    df.to_excel(writer, startrow=0, sheet_name=sheet_title, index=False)
