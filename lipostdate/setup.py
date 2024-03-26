from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python package for extracting the exact date from the linkedin post URLs'
LONG_DESCRIPTION = '''LinkedIn Post Date Extractor is a Python package designed to streamline
the process of extracting the exact date from LinkedIn post URLs.
With the growing importance of timely information and the prevalence of LinkedIn as a platform for professional networking and content sharing,
this package provides a convenient solution for users who need to quickly retrieve the posting date of a LinkedIn article or post.
'''

setup(
        name="lipostdate", 
        version=VERSION,
        author="Garv Saxena",
        author_email="garvsaxena185@gmail.com",
        url  = "https://github.com/Volcano-Dragon/lipostdate",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        py_modules=['lipostdate'],
        install_requires=[],        
        keywords=['linkedin', 'linkedin post dates', 'linkedin post extraction', 'linkedin post url'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
