from setuptools import setup, find_packages


setup(
    name="pgtestapp",
    version="0.1",
    description="Application to test PostgreSQL replication.",
    packages=find_packages(),
    install_requires=["gunicorn"],
)
