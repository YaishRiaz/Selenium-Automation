import os
import pathlib

class Config:
    home = pathlib.Path(__file__).parents[1]
    CHROME_DRIVER_PATH = str(pathlib.Path(__file__).parent) + "\\drivers\\chromedriver.exe"
    BROWSER_TYPE = "chrome"

    DRIVERS = [{
        'browser': 'chrome',
        'path': os.path.join(home) + "\\drivers\\chromedriver.exe"
    }, {
        'browser': 'edge',
        'path': os.path.join(home) + "\\drivers\\msedgedriver.exe"
    }]

