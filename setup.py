import os
import sys
import matplotlib
from setuptools import find_packages
from cx_Freeze import setup, Executable


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'requirements.txt')) as f:
    requires = f.read().splitlines()

# MSI shortcut folder to create the start in directory.
shortcut_table = [(
    "DesktopShortcut",        # Shortcut
    "DesktopFolder",          # Directory_
    "Openroast",              # Name
    "TARGETDIR",              # Component_
    "[TARGETDIR]Openroast.exe",# Target
    None,                     # Arguments
    None,                     # Description
    None,                     # Hotkey
    None,                     # Icon
    None,                     # IconIndex
    None,                     # ShowCmd
    'TARGETDIR'               # WkDir
)]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["openroast"],
     "includes": ["matplotlib", "serial", "distutils", "matplotlib.backends.backend_qt5agg"],
     "include_files": [
        "static",
        "openroast/views",
        "openroast/controllers",
        "LICENSE",
        (matplotlib.get_data_path(), "mpl-data")],
     "include_msvcr": True
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name='Openroast',
    version='1.0.0',
    description='An open source, cross-platform application for home coffee roasting',
    long_description=README,
    license='GPLv3',
    author='Roastero',
    url='http://roastero.com',
    author_email='admin@roatero.com',
    include_package_data=True,
    options = {
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
        "bdist_mac": {"iconfile": "static/icons/openroast-mac.icns"}},
    executables = [
        Executable('Openroast.py')],
    zip_safe=False,
    data_files=matplotlib.get_py2exe_datafiles(),
    packages=find_packages(),
    install_requires=requires)
