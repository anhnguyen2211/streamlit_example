import sys
import yaml
import mysql.connector


CONFIG_FILE = "../configs/.database.yaml"


def get_data_base(db_info):
    try:
        data_base = mysql.connector.connect(host=db_info["host"],
                                            user=db_info["username"],
                                            passwd=db_info["password"],
                                            database=db_info["database"])
    except RuntimeError:
        # sys.exit("Cannot connect to server {}\n".format(db_info["name"]))
        return None
    return data_base


class Database:
    def __init__(self, file_path=CONFIG_FILE):
        with open(file_path, "r") as stream:
            try:
                databases = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        database = {}
        list_db_name = []
        for db_info in databases.values():
            database[db_info["name"]] = get_data_base(db_info)
            list_db_name.append(db_info["name"])
        self.database = database
        self.list_db_name = list_db_name


if __name__ == '__main__':

    db = Database()
    print(db.database)
