from setuptools import setup, find_packages

def long_description():
    with open("README.md", "r") as fhandle:
        return fhandle.read()

setup(
    name='discord_database',

    version='1.0.3',

    description='a database for discord.py',

    long_description=long_description(),
    long_description_content_type='text/markdown',

    url='https://cutebear.dynv6.net',

    author='cutebear',
    author_email='cutebear@cutebear.dynv6.net',

    license='MIT',
    
    packages=find_packages(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)