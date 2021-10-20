import requests as rq
from advice.errors import * 
import json, random
from advice.constants import BASE_URL


class Url:
  # def __init__(self):

  #   self.base_url = BASE_URL
  #   self.headers = {'content-type': 'application/json'}


  # def base_url(self):
  #   return self.base_url <- Saldy none of this code works..

  def status(self):
        try:
                response = rq.head(BASE_URL)
                # print(response.status_code)

                if response.status_code >= 500:
                    raise NotRecognizable('500 or more server is gone')
                elif response.status_code == 404:
                    return f"404 error"
                elif response.status_code == 200:
                  return response.status_code
                return response.status_code
               # return response.status_code
        except rq.ConnectionError:
            print('failed to connect')
  
  def requestrandomurl(self):
    '''
    No arguments, this will return any random slip_id'''
    headers = {'content-type': 'application/json'}
    S = rq.Session()
    status = self.status()
    if status:
      res = S.get(BASE_URL, headers=headers).json()
      print(res)
    else:
      raise NotRecognizable('404')


# t = Url()

# t.requestrandomurl()