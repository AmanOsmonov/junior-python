import bs4
from selenium import webdriver
from django.core.management.base import BaseCommand
from main.models import UserRequestRezult, UserRequest


class Command(BaseCommand):
    help = 'parsing GitHub'

    def handle(self, *args, **options):

        HOST = 'https://github.com/'
        #a=UserRequest.objects.order_by('-link')[:1]
        driver = webdriver.Chrome(executable_path='D:\питон проекты\Parser\chromedriver.exe')
        driver.get('https://github.com/petersaalbrink/cpython/pulls')

        ht = driver.page_source
        soup = bs4.BeautifulSoup(ht, 'html.parser')
        element = soup.find_all('div', class_="Box-row")

        pull = []

        for i in element:
            pull.append(
                {
                    'title': i.find('a', class_="Link--primary").get_text(),
                    'link': HOST + i.find('a', class_="Link--primary").get('href'),

                }
            )

        driver.quit()
