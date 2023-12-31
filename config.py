from configparser import ConfigParser
# файл конфигурации
# Тут необходимо указать абсолютный путь к database.ini
file_exp = "F:/python projects/Course_work_5_postgreSQL/database.ini"


def config(filename=file_exp, section="postgresql"):
    # create a parser
    parser = ConfigParser()

    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db
