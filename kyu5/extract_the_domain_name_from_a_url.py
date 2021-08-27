import re


def domain_name(url):
    url = url.replace("www.", '')
    try:
        return url.split('//')[1].split('.')[0]
    except:
        return url.split('.')[0]


# With Regex


def domain_name(url):
    return re.search("(https:?://)?(www\d?\.)?(?P<name>[\w-]+)\.", url).group('name')


# Best solution so far
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name("www.xakep.ru"))
print(domain_name("qr0rdcelaug2whro1gnjzm.it"))
print(domain_name("http://www.codewars.com/kata/"))
print(domain_name("http://google.co.jp"))
