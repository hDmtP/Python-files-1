from unittest import result
from craigslist import CraigslistJobs
jobs = CraigslistJobs(site='sfbay', area='sby', category='sof',filters={'is_internship': True, 'employment_type': ['full-time', 'part-time']})

for result in jobs.get_results():
    print(result)
# ImportError: cannot import name 'ZipFile' from partially initialized module 'zipfile' (most likely due to a circular import)

'''
CATEGORY => ARGUMENTS

jobs => site='sfbay', area='sby', category='sof',
                      filters={'is_internship': True, 'employment_type': ['full-time', 'part-time']}
housing => site='sfbay', area='sfc', category='roo',
                         filters={'max_price': 1200, 'private_room': True}
more available on => "https://github.com/juliomalegria/python-craigslist"
'''

