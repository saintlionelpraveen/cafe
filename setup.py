from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="cafe",
    version="0.0.1",
    description="this is for the L:aura Cafe Inventory System",
    author="Praveen",
    author_email="jaga03038@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
