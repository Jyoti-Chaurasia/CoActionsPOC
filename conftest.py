import outcome
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.util import take_screenshot
from datetime import datetime

# Generate a timestamp
driver= None

@pytest.fixture(scope="function")
def driver():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.quit()


# @pytest.hookimpl( hookwrapper=True )
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin( 'html' )
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr( report, 'extra', [] )

#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr( report, 'wasxfail' )
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports\Screenshots')
#             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
#             file_name = os.path.join( reports_dir, f"_failed_at_{timestamp}.png" ).replace('\\', '/')
#             print( "file name is " + file_name )
#             take_screenshot( driver, file_name )
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append( pytest_html.extras.html( html ) )
#         report.extras = extra

