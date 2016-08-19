from setuptools import setup

setup(name='parse_checks',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/rollerr/parse_checks',
      author='rollerr',
      author_email='notyet@aol.com',
      license='MIT',
      packages=['parse_checks',
                'parse_checks/vyos',
                'parse_checks/utilities'],
      zip_safe=False,
      install_requires=['pyyaml'],
      extras_require={
        'test': ['pytest>=2.6.0',]
      },
)
