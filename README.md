# ReportBot-glory-to-Ukraine
This bot is created for make mass report of some russian channel, to help Ukraine.
I have read the list, of the Youtube Channel to report, created by the ukraine IT army that said: "Report this channels". I have made a bot that reports automatically and also forever.
 

## Installation
Download on your computer the file: "russiaDestroyer.py"

## Tools that you need
    -Python3
    -Pip3
    -Selenium (pip install selenium)
    -IDE (I used VSCode)
    -Create a new Google Account 
    -Chromedriver (https://chromedriver.chromium.org/downloads)
If you have problems with the installation of Chromedriver and selenium watch this video: https://youtu.be/


## Usage
The parts below are the parts of code that you have to modify. The other parts need to be the same as the "russiaDestroyer.py" file.
```python
# Insert the Path of your webdriver in the quotation marks 
driver = webdriver.Chrome('PATH')

# Insert your new mail of the google account in the quotation marks after "send_keys"
driver.find_element_by_xpath('//input[@type="email"]').send_keys('EMAIL')

# Insert the password of your new  google account in the quotation marks after "send_keys"
driver.find_element_by_xpath('//input[@type="password"]').send_keys('PASSWORD')

# Insert the url of the "about" page of the youtube channel that you want to report. REPORT ONLY THE RUSSIAN CHANNELS THAT ARE IN THE LIST BELOW.
 driver.get('CHANNEL ABOUT PAGE')

# Choose the times that you want to repeat the report in the brackets after "range"
for i in range('NUMBER'):
         __russiaDestroyer__()

```
## List of the Channel to Report
https://www.youtube.com/channel/UCX9-cJy8dZWDI8hCnmahuLA
https://www.youtube.com/c/Russia24TV
https://www.youtube.com/c/TASSagency
https://www.youtube.com/user/rianovosti
https://www.youtube.com/channel/UC2D0dmLHKbIe9aACnlcTLPg
https://www.youtube.com/channel/UCWAK-dRtTEjnQnD96L6UMsQ
https://www.youtube.com/channel/UCRds47MZ1Ng7KCLseg2TkWA
https://www.youtube.com/channel/UC8Nl7TQLC6eX8MTRCuAw3SA
https://www.youtube.com/channel/UCGRcod_jR4sC9XUMLCv4GJQ
https://www.youtube.com/channel/UCSqO8lV-ric7ow5G5q9roWw
https://www.youtube.com/channel/UCdyhZX5wt6B6dSIAT7X9dNw
https://www.youtube.com/channel/UCRHhScZmH-SfBin8tbTixPA
https://www.youtube.com/channel/UC3rZ3DKoeiccjl-e-lams_g
https://www.youtube.com/channel/UCJvDYmmZDbeDy5N_aBxXjpA
https://www.youtube.com/channel/UCMTaJV_Gyp1YOWJwSNa0wRw
https://www.youtube.com/channel/UC8lCS8Ubv3t0-Tf4IYLioTA
https://www.youtube.com/c/ZimaLive
https://www.youtube.com/channel/UCQ4YOFsXjG9eXWZ6uLj2t2A


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache](https://choosealicense.com/licenses/apache/)
