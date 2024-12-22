RESULT_PATH = 'msdt-3/result.json'
CSV_PATH = 'msdt-3/4.csv'
LOGS = 'msdt-4/logs.txt'
REGULAR = {
    "telephone"  : "^\\+7-\\(\\d{3}\\)-\\d{3}-\\d{2}-\\d{2}$",
    "height"     : "^[0-2]\\.\\d{2}$",
    "snils"      : "^\\d{11}$",
    "identifier" : "^\\d{2}\\-\\d{2}\\/\\d{2}$",
    "occupation" : "[a-zA-Zа-яА-ЯёЁ -]+",
    "longitude"  : "^-?(180(\\.0+)?|1[0-7]\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)$",
    "blood_type" : "^(O|A|B|AB)[\\+\u2212]$",
    "issn"       : "^\\d{4}\\-\\d{4}$",
    "locale_code": "^[a-zA-Z]+(-[a-zA-Z]+)*$",
    "date"       : "^(19|20)\\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01])$"
}