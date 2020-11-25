"""
Configuring application
"""
import configparser

# Read the application configuration file
print("configuring")
config_parser = configparser.ConfigParser()
config_parser.read('ghibli.ini')
print("configured")
