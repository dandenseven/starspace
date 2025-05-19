from configparser import  ConfigParser
import os


def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    if not parser.has_section(section):
        raise Exception(f'Section {section} not found in the {filename} file')
    
    # Read config values
    db_config = {param[0]: param[1] for param in parser.items(section)}
    
    # Add sensitive values from environment
    db_config['user'] = os.environ.get('DB_USER')
    db_config['password'] = os.environ.get('DB_PASS')

    return db_config

if __name__ == '__main__':
    config =load_config()
    print(config)

    


