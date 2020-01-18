# https://github.com/hhru/api/blob/master/docs/vacancies.md#search
# HH api

import requests
import re
import collections

class HhApi:
    def __init__(self, *args):
        self._url = args[0]
        self.params={}

    def get_all_info(self, *args, **kwarg):
        
        type_print = False 
        if args.__len__()>0:
            type_print =  args[0]
        self.params = kwarg['params']
        rez = requests.get(self._url, params=self.params).json()
        found, pages, per_page = -1, -1, -1

        try:
            self.found = rez['found']
            self.pages = rez['pages']
            self.per_page = rez['per_page']
            if type_print:
                print("*"*40,'\n'
                    ,'found = {}  pages = {}  per_page = {} '.format(self.found, self.pages, self.per_page)
                    ,'\n',"*"*40)
        except expression as identifier:
            print('Error  - Ошибка запроса')                        

    def get_request_page(self, *args, **kwarg):
        self.params['page'] = args[0]

        rez=requests.get(self._url, params=self.params).json()
        try:
            self.all_page = rez['items']
            return self.all_page
        except  KeyError:       # (NameError):
            return None

    def __parsing_(self, s):
            s=s.lower().replace("с+",'xq').replace("с#",'xw')

            q=  re.sub(r' +', ' '
            , re.sub(r'[^\w\s]+|[\d]+', r''
                , re.sub(r"[а-яА-Я]+",""
                    ,s.replace("<highlighttext>","").replace("</highlighttext>","")))).strip()
            q= q.replace('xq','c+').replace('xw','c#')
            return list(q.split(' '))

   
    def filtr_str(self, page_):
        rez = HhApi.get_request_page(self, page_)
        ls=[]
        for it in range(len(rez)):
#            print('=== {} ==='.format(it))
            x = str(rez[it]['snippet']['requirement'])
            if x != "None":
#                print("*"*40,'\n',x)
                ls= ls + HhApi.__parsing_(self, x)
            x = (rez[it]['snippet']['responsibility'])
            if x != None:
#                print("*"*40,'\n',x)
                ls = ls + HhApi.__parsing_(self, x)
        return ls