import os
import configparser

# os.path.dirname(__file__) 현재 위치해있는 경로
lib_dir = os.path.dirname(__file__)
env_config = configparser.ConfigParser()
env_config.read(lib_dir + '/config.ini', encoding='utf-8')

api_key = env_config['AUTH']['api_key']
api_secret = env_config['AUTH']['api_secret']
protocol = env_config['SERVER']['protocol']
domain = env_config['SERVER']['domain']
prefix = env_config['SERVER']['prefix'] and env_config['SERVER']['prefix'] or ''


def get_url(path):
    url = '%s://%s' % (protocol, domain)
    if prefix != '':
        url = url + prefix
    url = url + path
    return url
