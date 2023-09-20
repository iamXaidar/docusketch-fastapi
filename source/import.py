from utils import import_to_psql, add_row_to_xlsx
from config import settings

# Import executable module
is_excel = True
if not is_excel:
    data_dict = {"item_id": [i for i in range(1, 100)], "name": [f"Random Item {i}" for i in range(1, 100)]}
    add_row_to_xlsx(file_name="init.xlsx", source=data_dict)

import_to_psql(excel_table_path=f"{settings.BASE_DIR}/data/init.xlsx")
