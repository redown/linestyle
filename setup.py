import setuptools

with open('README.md', 'r', encoding='utf-8') as fd:
    desc_data = fd.read()

setuptools.setup(
    name='linestyle',
    version='0.0.1',
    author='redown',
    author_email='redown@yeah.net',
    description='A simple example',
    long_description=desc_data,
    long_description_content_type='text/markdown',
    url='https://github.com/redown/linestyle',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
)
