from setuptools import setup

setup(
    name='miab',
    version='0.1.0',
    py_modules=['miab'],
    install_requires=[
		'click==8.1.3', 
		'requests==2.28.1', 
		'python-dotenv==0.21.0'
    ],
    entry_points={
        'console_scripts': [
            'miab = main:cli',
        ],
    },
)
