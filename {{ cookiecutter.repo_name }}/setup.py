import glob
from setuptools import setup, find_packages
import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(APP_DIR, 'README.md')
LICENSE_PATH = os.path.join(APP_DIR, 'LICENSE')
REQUIREMENTS_PATH = os.path.join(APP_DIR, 'requirements.txt')

print "APP_DIR: ", APP_DIR
print "README_PATH: ", README_PATH
print "LICENSE_PATH: ", LICENSE_PATH
print "REQUIREMENTS_PATH: ", REQUIREMENTS_PATH


with open(REQUIREMENTS_PATH) as f:
    required = f.read().splitlines()

setup(
    name='{{ cookiecutter.repo_name.replace('-','_') }}',
    version='{{ cookiecutter.version }}',  # Required
    license='GPL-2.0',
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description_content_type="text/markdown",
    url="https://{{ cookiecutter.version_control }}.com/{{ cookiecutter.git_organization }}/{{ cookiecutter.repo_name }}",
    packages=find_packages("src", exclude=['contrib', 'docs', 'tests']),  # Required
    package_dir={"": "src"},
    py_modules=[os.path.splitext(os.path.basename(i))[0] for i in glob.glob("src/*.py")],
    # package_data={'': ['LICENSE', 'logger.conf']},
    include_package_data=True,
    install_requires=required,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Flask",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 2.7",
        "Operating System :: POSIX",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ]
)
