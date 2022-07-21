from selenium import webdriver
from GeicoTestScripts import Auto_Geico_Test


class PageLoadTimer(Auto_Geico_Test):

    def __init__(self, web_page):
        self.WebPage = web_page

    def RunPerformanceTest(self, trials):
        back_end_load = []
        front_end_load = []
        for i in range(trials):
            hyperlink = self.WebPage
            driver = webdriver.Chrome()
            driver.get(hyperlink)
            #Use Navigation Timing  API to calculate the timings that matter the most
            navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            domComplete = driver.execute_script("return window.performance.timing.domComplete")
            #Calculate the performance
            backendPerformance_calc = responseStart - navigationStart
            frontendPerformance_calc = domComplete - responseStart
            back_end_load.append((backendPerformance_calc))
            front_end_load.append((frontendPerformance_calc))
            print("Back End: %s" % backendPerformance_calc)
            print("Front End: %s" % frontendPerformance_calc)
            driver.quit()

            i = i + 1

        print(back_end_load)
        print(front_end_load)
        return

