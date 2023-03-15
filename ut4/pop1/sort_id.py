# **********************************
# ORDENANDO IDS EN UNA BASE DE DATOS
# **********************************


def sort_id(db: list) -> list:
    for item in db:
        id = item['id']
        item['id'] = id
    return db
