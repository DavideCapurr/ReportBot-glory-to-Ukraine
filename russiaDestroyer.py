from selenium import webdriver
from time import sleep

def __russiaDestroyer__():

        driver = webdriver.Chrome('WEBDRIVER PATH')
        driver.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dit%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253Fgl%253Dit%2526hl%253Dit&hl=it&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        sleep(2)
        driver.find_element_by_xpath('//input[@type="email"]').send_keys('MAIL')
        driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(2)
        driver.find_element_by_xpath('//input[@type="password"]').send_keys('PASSWORD')
        driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        driver.get('YOUTUBE CHANNEL ABOUT PAGE ')
        sleep(5)
        driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-about-metadata-renderer/div[2]/div/ytd-button-renderer/a/yt-icon-button/button/yt-icon').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[3]/tp-yt-paper-item').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="yt-options-renderer-options"]/tp-yt-paper-radio-button[6]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="next-button"]/a').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="next-button"]/a').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-multi-page-menu-renderer/div[3]/div[2]/ytd-report-channel-modal-footer-renderer/ytd-button-renderer[2]/a/tp-yt-paper-button').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[2]/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string').click()
        sleep(2)


for i in range(NUMBER OF REPORT):
         __russiaDestroyer__()
