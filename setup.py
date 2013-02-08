from setuptools import setup, find_packages

tests_require = [
    'manuel',
    'zope.testing',
    ]


setup(
    name='wherefore',
    author='Benji York',
    author_email='benji@benjiyork.com',
    description='Ever wondered where a value came from in your program?  ' +
        'Trace down the origin of any value with Wherefore.',
    version='0',
    install_requires=[
        # 'docopt', since docopt isn't packaged and is just one file, I
            # stashed a copy inside the wherefore directory
        'setuptools',
    ],
    tests_require = tests_require,
    extras_require={
        'tests': tests_require,
        },
    zip_safe=False,
    package_dir={'':'.'},
    packages=find_packages('.'),
    include_package_data=True,
    )
