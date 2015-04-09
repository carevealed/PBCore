from setuptools import setup, find_packages

setup(
    name='CAVPP_PBCore_Tools',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/cavpp/PBCore',
    install_requires=['OneSheet == 0.1.3.26'],
    license='GPL',
    author='California Audio Visual Preservation Project',
    author_email='hborcher@berkeley.edu',
    description='Tool for building PBCore from data exported from CONTENTdm.',
    entry_points={'console_scripts': ['makepbcore = pbcore.scripts.pbcore_csv:main', 'tvs2csv = pbcore.scripts.tsv2csv:main']},
    include_package_data=True,
    package_data={"": ['pbcore/scripts/gui/images/CAVPPcolor.gif', 'pbcore/settings/pbcore-csv-settings.ini']}
)
