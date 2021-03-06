from advice.constants import BASE_URL, see_query
from advice.errors import * 
import requests
from .base import * 
from .classes import * 
import json 

class Search(Base):
  def get_all_search(self, query: str = 'spiders'):
    S = requests.Session()
    url = f'{BASE_URL}/search/{query}'
    res = S.get(url).json()
    return print(res)

  def search_times(self, total_res: int = 1, search: str = 'spiders'):
    '''
    total_res: int: defaults to 1 for the many times it will be called
    search: str = spiders(the starting query for the search)
    If the string doesn\'t exist or total_res has an int larger than the value it needs it will deploy a kepypagerror'''
    
    S = requests.Session()
    url = f'{BASE_URL}/search/{search}'
    res = S.get(url).json() 
    n = 0
    # r = see_query(total_res = total_res)
    for i in range(total_res):
      if total_res > int(res['total_results']):
        raise keypageError
      elif int(res['total_results']) > 1:
        print(res['slips'][n]['advice'])
        n += 1
      else:
        print(res['slips'][n]['advice'])
        # return res['slips'][n]['advice']

# t = Search()

# t.get_all_search()
# t.search_times()