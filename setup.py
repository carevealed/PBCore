from setuptools import setup, find_packages
long_description = open('README.md').read()

setup(
    name='CAVPP_PBCore_Tools',
    version='0.1.6.4',
    packages=find_packages(),
    url='https://github.com/cavpp/PBCore',
    install_requires=['OneSheet >= 0.1.5.7'],
    license='GPL',
    author='California Audio Visual Preservation Project',
    author_email='hborcher@berkeley.edu',
    description='Tool for building PBCore from data exported from CONTENTdm.',
    long_description=long_description,
    entry_points={'console_scripts': ['makepbcore = PBCore.scripts.pbcore_csv:main', 'tsv2csv = PBCore.scripts.tsv2csv:main']},
    include_package_data=True,
    zip_safe=False,
    package_data={"PBCore/scripts/images": ['CAVPPcolor.gif'], "PBCore": ['settings/pbcore-csv-settings.ini']}
)
