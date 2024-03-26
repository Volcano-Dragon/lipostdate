# lipostdate

## Overview
The lipostdate.py module is a Python library designed to streamline the process of extracting the exact date from LinkedIn post URLs. With the growing importance of timely information and the prevalence of LinkedIn as a platform for professional networking and content sharing, this package provides a convenient solution for users who need to quickly retrieve the posting date of a LinkedIn article or post.


## Getting Started

### Installation

```
pip install lipostdate
```


### Quick Start Example

```python
import lipostdate as lp
# getDate(link=None, ignore_exception=False)

#prints the exact date and time of the post
print(lp.getDate('https://www.linkedin.com/posts/volcano-dragon2004_linkedinskillassessment-activity-6966492522810339328-seGq?utm_source=share&utm_medium=member_desktop'))
#Output: ['Sat Aug 20 02:04:08 2022']

```


### Ignore the exception for multiple occurrences of a 19-digit number.

Post URLs contain 19-digit numbers, in which the first 41 bits are Unix time stamps. 

***Example of 19-digit number***: ```https://www.linkedin.com/posts/volcano-dragon2004_linkedinskillassessment-activity-6966492522810339328-seGq?utm_source=share&utm_medium=member_desktop```<br>
This link contains "6966492522810339328" 19-digit number.

When more than one occurrence of a 19-digit number is in a link, the "ignore_exception=True" argument can ignore the exception.

**Set ignore_exception = True**: To ignore the exception for multiple occurrences of a 19-digit number. (Default = **False**)

```python
import lipostdate as lp
# getDate(link=None, ignore_exception=False)

#prints the exact date and time of the post
#passing a link with 2 occurrences of 19-digit number
print(lp.getDate('https://www.linkedin.com/posts/volcano-dragon6970593094522023937_linkedinskillassessment-activity-6966492522810339328-seGq?utm_source=share&utm_medium=member_desktop', True))
#Output: ['Wed Aug 31 09:38:21 2022', 'Sat Aug 20 02:04:08 2022']
```
