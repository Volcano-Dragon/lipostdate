"""The lipostdate.py module is a Python library designed to streamline the process of extracting the exact date from LinkedIn post URLs.
With the growing importance of timely information and the prevalence of LinkedIn as a platform for professional networking and content sharing,
this package provides a convenient solution for users who need to quickly retrieve the posting date of a LinkedIn article or post.


GitHub Repositry link: https://github.com/Volcano-Dragon/lipostdate
Module Author: Garv Saxena
Garv Saxena email: garvsaxena185@gmail.com
"""

import time #time is required for converting the final seconds to the exact date
import re #regex is used for the pattern matching

def getDate(link = None, ignore_exception = False):
    '''
    From the post URL, this function extracts the 19-digit ID, where the first 41 bits represent the Unix time stamp.
 
    Parameters:
        link = URL of the linkedin post in string.
            Default: None
        ignore_exception = To ignore the exception if the post URL contains more then one occurrence of a 19-digit number.
            Default: False
    Returns:
        dates = list of all exact dates from the post URL
    '''

    assert bool(link), "No link given, for date extraction"
    assert type(link)==str, f"'str' required in link, Given {type(link)}"
    assert "linkedin.com" in link.lower(), "Link is not from the LinkedIn domain, it is invalid"
    result = re.findall('[0-9]{19}', link) #Searching for the 19-digit number in the post URL
    assert len(result)!=0, "Unable to find 19-digit number, invalid link"
    assert ignore_exception or len(result)==1, f"""The link contains more than one occurrence of a 19-digit number; to ignore this exception, pass the argument "ignore_exception = True" or check the link again.\nGiven link contains the following 19-digit numbers:\n{result}"""

    dates = []
    for i in result:
        dates.append(time.ctime((int(i)>>len(bin(int(i)))-43)//1000)) #extracting and converting(to exact date) the first 41 bits from the 19-digit integer number

    return dates



