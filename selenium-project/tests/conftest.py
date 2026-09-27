import os
import pytest
from utils import get_driver

@pytest.fixture
def driver():
    """Fixture to start and quit browser for each test"""
    driver_instance = get_driver()
    yield driver_instance
    driver_instance.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically capture screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver_instance.save_screenshot(screenshot_path)
            
            # Attach to HTML report
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra
