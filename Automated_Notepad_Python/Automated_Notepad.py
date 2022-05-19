from Main import Ui_AutoNotepad
from Glossary import Dictionary
from PyQt5 import QtWidgets 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, os, time, re


#setup imported Ui from Qt Designer converted 'Main.py'
class MainWindow(QtWidgets.QMainWindow, Ui_AutoNotepad):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        
        self.copy_button.clicked.connect(self.copy)
        self.search_button.clicked.connect(self.search)
        self.reset_button.clicked.connect(self.reset)
        self.reverse_email_button.clicked.connect(self.reverse)
        self.search_email_button.clicked.connect(self.emailsearch)
        self.JT_crosscheck_button.clicked.connect(self.JT_Crosscheck)
        self.designation = ''
        self.specialties = []
        self.degrees = []
        self.firstName = ''
        self.lastName = ''


    def namesake_search(self):
        namesake = '^(Namesake)s?\S'



    def kol_info_search(self):
        KP_name = '(KOL):?|(KP):?'


    
    #Copies necessary information from profile 
    def copy(self):
        target = self.profile_link.text()
        

#sample only, still needs major fix

        affiliations = []
        namesakes = []
        option = Options()
        option.add_experimental_option('debuggerAddress','localhost:9222')
        driver= webdriver.Chrome(options=option)
        degrees = driver.find_element(By.CLASS_NAME, 'degree')
        driver.get(target)


    #Checks for MD (current code does not return boolean)
        has_MD = re.search('Doctor of Medicine', driver.page_source.text())
        if (has_MD == object):
            self.designation = '病院'
        else:
            self.designation = '研究'

        try:
            

            comment_box_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[5]/a/i'))
            )

            comment_box_button.click()


            originalName = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[1]/h6'))
            )

            last_name = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[1]/h4/a/span[2]'))
            )

            first_name = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[1]/div[1]/h4/a/span[1]'))
            )

            affiliation1 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[3]/div/span[2]'))
            )


            affiliation2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[3]/div/span[3]'))
            )

            affiliation3 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[4]/div/span[2]'))
            )

            affiliation4 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[4]/div/span[3]'))
            )


            specialties = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div[2]/div[1]/div[2]/div[1]'))
            )

            specialties_list = specialties.find_element(By.XPATH, './/')


            kolID = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/dirt/dirt-profile/div/section/dirt-profile-detail/section/div/div[1]/div/div[3]/div[6]/div/span[2]'))
            )


            self.original_name.setText(originalName.text)
            self.romanised_name.setText(last_name.text + ' ' + first_name.text)
            self.affiliations_text.setText(affiliation1.text + ' ' + affiliation2.text + ' ' + '\n' + affiliation3.text + ' ' + affiliation4.text)
    #needs fixing still
            for specialty in specialties:
                self.keywords_text.setText(specialty + '\n')
            self.KOL_ID.setText(kolID.text)

            self.firstName = first_name.text
            self.lastName = last_name.text
            #self.namesakes_text.setText(namesakes.text)


        except:
            print('Error')
            time.sleep(5) 


    #Send search data to google search
    def search(self):
        name = ''
        specialty_returned = ''

        #for specialty in self.specialties:
            

        if self.original_name.text() == '':
            name = self.romanised_name.text()
        else:
            name = self.original_name.text()

        os.environ['webdriver.chrome.driver'] = '/usr/bin'
        #s= Service(executable_path='/usr/bin/google-chrome-stable')
        option = Options()
        option.add_experimental_option('debuggerAddress','localhost:9222')
        driver = webdriver.Chrome(options=option)
        driver.execute_script("window.open('about:blank', 'PA1');")
        driver.switch_to.window('PA1')
        driver.get('https://google.com')

        try:
            searchbox = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )

            searchbox.send_keys('{name} {designation}'.format(name=name, designation=self.designation))
            searchbox.send_keys(Keys.RETURN)

            driver.execute_script("window.open('about:blank', 'PA2');")
            driver.switch_to.window('PA2')

            searchbox2 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )

        #Function still needs fixing (do not assign whole keyword text to specialty), array functionality will not work yet
            searchbox2.send_keys(name + ' ' + Dictionary[self.specialties[0]])
            searchbox2.send_keys(Keys.RETURN)


        except:
            print('Error')
            time.sleep(5)
        
  

    #Resets all info boxes to blank, Usable to close tabs?
    def reset(self):
        self.profile_link.setText('')
        self.romanised_name.setText('')
        self.original_name.setText('')
        self.affiliations_text.setText('')
        self.keywords_text.setText('')
        self.namesakes_text.setText('')
        self.reverse_email.setText('')
        self.search_email.setText('')
        self.KOL_ID.setText('')
        self.designation.setText('')
        self.specialties.setText('')
        self.degrees.clear()
        self.specialties.clear()
        self.firstName.setText('')
        self.lastName.setText('')

        
    #Reverses email 
    def reverse(self):
        corrected_email = self.reverse_email.text()[::-1]
        self.reverse_email.setText(corrected_email)

    #Searches google queries for email according to recommended steps
    #How to capture PA name?
    def emailsearch(self):
        url = self.search_email.text()
        original_name = self.original_name.text()
        english_name = self.romanised_name.text()
        option = Options()
        option.add_experimental_option('debuggerAddress','localhost:9222')
        driver = webdriver.Chrome(options=option)

        driver.execute_script("window.open('about:blank', 'email1');")
        driver.switch_to.window('email1')
        driver.get('https://google.com')


        try:
            searchbox1 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox1.send_keys('{english_name} {url}'.format(english_name=english_name, url=url))
            searchbox1.send_keys(Keys.RETURN)
    


            driver.execute_script("window.open('about:blank', 'email2');")
            driver.switch_to.window('email2')
            driver.get('https://google.com')
            searchbox2 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox2.send_keys('{} @ email'.format(lastName=self.lastName))
            searchbox2.send_keys(Keys.RETURN)

            driver.execute_script("window.open('about:blank', 'email3');")
            driver.switch_to.window('email3')
            driver.get('https://google.com')
            searchbox3 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox3.send_keys('{lastName} @ email {url}'.format(lastName=self.lastName, url=url))
            searchbox3.send_keys(Keys.RETURN)


            driver.execute_script("window.open('about:blank', 'email4');")
            driver.switch_to.window('email4')
            driver.get('https://google.com')
            searchbox4 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox4.send_keys('{english_name} @ email {specialties}'.format(english_name=english_name, specialties=self.specialties[0]))
            searchbox4.send_keys(Keys.RETURN)


            driver.execute_script("window.open('about:blank', 'email5');")
            driver.switch_to.window('email5')
            driver.get('https://google.com')
            searchbox5 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox5.send_keys('{original_name} @ email {specialties}'.format(original_name=original_name, specialties=Dictionary[self.specialties[0]]))
            searchbox5.send_keys(Keys.RETURN)



            driver.execute_script("window.open('about:blank', 'email6');")
            driver.switch_to.window('email6')
            driver.get('https://google.com')
            searchbox6 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox6.send_keys('{} メール'.format(original_name))
            searchbox6.send_keys(Keys.RETURN)


            driver.execute_script("window.open('about:blank', 'email7');")
            driver.switch_to.window('email7')
            driver.get('https://google.com')
            searchbox7 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox7.send_keys('site:https://ncbi.nlm.nih.gov {} email'.format(english_name))
            searchbox7.send_keys(Keys.RETURN)


        except:
            print('Error')
            time.sleep(5)
    
    #Sends google queries to check for other JTs KP might have (possibly higher for example)
    def JT_Crosscheck(self):
        name = ''

        if self.original_name.text() == '':
            name = self.romanised_name.text()
        else:
            name = self.original_name.text()

        url = self.search_email.text()
        option = Options()
        option.add_experimental_option('debuggerAddress','localhost:9222')
        driver = webdriver.Chrome(options=option)

        driver.execute_script("window.open('about:blank', 'JT1');")
        driver.switch_to.window('JT1')
        driver.get('https://google.com')

        try:
            searchbox = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox.send_keys('site:{url} {name} 部長 科長 センター長'.format(url=url,name=name))
            searchbox.send_keys(Keys.RETURN)


            driver.execute_script("window.open('about:blank', 'JT2');")
            driver.switch_to.window('JT2')
            driver.get('https://google.com')
            searchbox2 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
            )
            searchbox2.send_keys('site:{url} {name} 医員 医長'.format(url=url,name=name))
            searchbox2.send_keys(Keys.RETURN)

        except:
            print('Error')
            time.sleep(5)
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())