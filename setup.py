import setuptools
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="Dbase_connectors",
    version="0.1.0",
    author="Lakhdar Belkharroubi",
    packages=["Dbase_connectors"],
    install_requires=[
        'mysql-connector-python',
        'psycopg2',
        'pyodbc',
    ],
    long_description = long_description,
    long_description_content_type='text/markdown'
)