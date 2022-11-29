from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='My Grader',
      description='Tools for automated grading with python.',
      long_description=readme(),
      keywords='grade grading student assignment',  
      license='MIT',
      packages=['gradepy'],  
      include_package_data=True,
      zip_safe=False)
