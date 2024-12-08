import os, logging, datetime, subprocess

logging.basicConfig(
    filename='./clean.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
    level=logging.INFO
)
logger=logging.getLogger(__name__)

BASE_PATH = os.path.dirname(__file__)
DOWNLOADER_PATH = os.path.join(BASE_PATH, "downloaders")
# STORE_PATH = os.path.join(DOWNLOADER_PATH, 'temp')
RESULTS_TEMP = '/mnt/bot_temp/temp/'
DOWNLOAD_TEMP = '/mnt/bot_temp/e2e/'
LITRES_PATH = os.path.join(DOWNLOADER_PATH, '_Elib2Ebook', 'LitresCache')

def clear_temp_folder():
    del_time = datetime.datetime.now() - datetime.timedelta(minutes=90)

    logger.warning(f'Очистка директории временных файлов {del_time}')

    del_time = del_time.timestamp()

    folders = os.listdir(DOWNLOAD_TEMP)
    for folder in folders:
        _f = os.path.join(DOWNLOAD_TEMP, folder)
        if os.path.isdir(_f):
            stats = os.stat(_f)
            if stats.st_mtime < del_time:
                logger.warning(f'Удаляем папку {folder}')
                q = subprocess.run(["rm", "-rf", _f])

def clear_temp_folder2():
    del_time = datetime.datetime.now() - datetime.timedelta(minutes=90)

    logger.warning(f'Очистка директории скачивания {del_time}')
    folders = os.listdir(RESULTS_TEMP)
    for folder in folders:
        _f = os.path.join(RESULTS_TEMP, folder)
        if os.path.isdir(_f):
            stats = os.stat(_f)
            if stats.st_mtime < del_time:
                logger.warning(f'Удаляем папку {folder}')
                q = subprocess.run(["rm", "-rf", _f])
    return


def clear_litres_folder():
    del_time = datetime.datetime.now() - datetime.timedelta(minutes=60)

    logger.warning(f'Очистка директории токенов Litres {del_time}')

    del_time = del_time.timestamp()

    tokens = os.listdir(LITRES_PATH)
    for token in tokens:
        _t = os.path.join(LITRES_PATH, token)
        stats = os.stat(_t)
        if stats.st_mtime < del_time:
            logger.warning(f'Удаляем токен {token}')
            q = subprocess.run(["rm", "-f", _t])
    return

clear_temp_folder()
clear_temp_folder2()
clear_litres_folder()