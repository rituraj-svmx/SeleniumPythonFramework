import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    ),
    parser.addoption(
        "--env_name", action="store", default="QA",
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    env_name = request.config.getoption("env_name")
    global driver
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()
    elif browser_name == "edge":
        driver = webdriver.Edge()

    if env_name == "DEV":
        driver.get("https://gemini.google.com/app")
    elif env_name == "QA":
        driver.get("https://rahulshettyacademy.com/upload-download-test/")
    elif env_name == "PROD":
        driver.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl")

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extras = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


