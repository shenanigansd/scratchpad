import json

import pandas

from databases.postgresql import connect
from utility import timestamp


def table_data(table_name):
    connection = connect()
    cursor = connection.cursor()

    rows = cursor.execute("SELECT * FROM %s" % table_name)

    keys = [k[0].decode('ascii') for k in cursor.description]
    results = [dict(zip(keys, row)) for row in rows]

    return results


def create_spreadsheet_from_table(table_name):
    pandas.read_json(json.dumps(table_data(table_name), default=str))\
        .to_excel("%s%s.xlsx" % (table_name, timestamp()), index=False)


def create_spreadsheet_for_all_tables():
    print('Generating...')
    writer = pandas.ExcelWriter('production-tracking_%s.xlsx' % timestamp(), engine='xlsxwriter')
    table_names = ['brandings', 'cart_preparations', 'catchings', 'designs', 'foldings', 'general_cleanings', 'hangers',
                   'hangings', 'ink_mixings', 'ka_order_pullings', 'orders', 'others', 'packagings',
                   'product_organizings', 'reclaimings', 'screen_cleanings', 'screen_makings', 'squeegees',
                   'taggings', 'tape_screens', 'upcs']
    for table_name in table_names:
        pandas.read_json(json.dumps(table_data(table_name), default=str)).to_excel(writer, sheet_name=table_name,
                                                                                   index=False)
    writer.save()
    print('Generated')


def get_name():
    employee_id = int(input('Enter an employee ID: '))

    connection = connect()
    cursor = connection.cursor()

    rows = cursor.execute("SELECT first_name, last_name FROM employees WHERE id=%d" % employee_id)

    keys = [k[0].decode('ascii') for k in cursor.description]
    results = [dict(zip(keys, row)) for row in rows]

    if not results:
        return 'Error: ID not found'
    else:
        return results[0].get("first_name") + " " + results[0].get("last_name")
