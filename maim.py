import requests
import pprint
import HHApi 
import json
import re
import collections

def sort_dan(ls):
    col=collections.Counter(ls)
    list_d = list(col.items())
    list_d.sort(key=lambda i: i[1], reverse = True )
    d=collections.OrderedDict()
    j=-1
    for i in list_d:
        j+=1
#        print(i[0], ':', i[1])
        if j < 10:
            d[i[0]]=i[1]
    return d

def form_dan1(param):
    rez=hh_api.get_all_info(False, params=params)
    xx = []
    x0 = []
    set_prog=['python', 'sql', 'git', 'linux', 'javascript', 'django', 'hive', 'sas', 'scrum', \
                'aosp', 'unix', 'ruby', 'php', 'nodejs', 'matlab', 'frontend', 'backend', 'web', \
                'office', 'qt', 'pyqt', 'java', 'c+', 'c#', 'experience', 'r', 'pandas', 'numpy'] 
    
    for i in range(0, 100):
        print(" ---> {}".format(i))
        xx =xx + hh_api.filtr_str(i)
    
    for it in xx:
        if it in set_prog:
            x0.append(it)
    return sort_dan(x0)


if __name__ == "__main__":
    url_vacancies='http://api.hh.ru/vacancies'
    hh_api = HHApi.HhApi(url_vacancies)

    params = {'text':"Python && Москва"}  #    
    pprint.pprint(form_dan1(params))

#Результат выполнения
#OrderedDict([('python', 1737),
#             ('sql', 412),
#             ('java', 248),
#             ('linux', 239),
#             ('experience', 134),  <- !!!!!!!  опыт!! 
#             ('r', 123),
#             ('web', 120),
#             ('git', 119),
#             ('javascript', 114),
#             ('django', 111)]) 

    params = {'text':"Python | sql | C+ | C# | linux | java | javascript | django | aosp | unix | ruby | php | nodejs | matlab \
                | git | hive | sas | scrum | frontend | backend | web | office | qt | pyqt | experience OR r | pandas | numpy && Москва"}  #    
    pprint.pprint(form_dan1(params))
#    OrderedDict([('sql', 618),
#             ('javascript', 605),
#             ('git', 525),
#             ('web', 423),
#             ('linux', 403),
#             ('experience', 344),
#             ('php', 308),
#             ('python', 296),
#             ('frontend', 277),
#             ('backend', 237)])

    params = {'text':"Python | sql | C+ | C# | linux | java | javascript | django | aosp | unix | ruby | php | nodejs | matlab \
                | git | hive | sas | scrum | frontend | backend | web | office | qt | pyqt | experience OR r | pandas | numpy"}  #    
    pprint.pprint(form_dan1(params))
#OrderedDict([('sql', 617),
#             ('javascript', 608),
#             ('git', 522),
#             ('web', 425),
#             ('linux', 405),
#             ('experience', 343),
#             ('php', 312),
#             ('python', 296),
#             ('frontend', 281),
#             ('backend', 237)])