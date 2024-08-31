from selene.support.shared import browser
from selenium import webdriver

options = webdriver.Chrome.options()
prefs = {
    'download.default_directory': '/path/to/save/downloads',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': False,
    'profile.default_content_settings.popups': 0,
    'profile.default_content_settings.media_playback_allow_popups': 0,
}
