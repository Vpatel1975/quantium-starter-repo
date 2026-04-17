import os
import pytest

# Path to chromedriver installed by webdriver-manager
CHROMEDRIVER_PATH = r"C:\Users\vpate\.wdm\drivers\chromedriver\win64\147.0.7727.57\chromedriver-win32\chromedriver.exe"
chromedriver_dir = os.path.dirname(CHROMEDRIVER_PATH)
os.environ["PATH"] = chromedriver_dir + os.pathsep + os.environ.get("PATH", "")


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    return chrome_options
