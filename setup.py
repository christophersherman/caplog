from setuptools import setup

setup(
    name='caplog',
    version='0.1.0',
    description='A simple command-line journal application',
    author='Christopher Sherman',
    author_email='sherm@fastmail.com',
    packages=['caplog'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'caplog=caplog.main:main'
        ]
    }
)
