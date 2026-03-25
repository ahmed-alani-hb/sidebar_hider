from setuptools import setup, find_packages

setup(
    name="sidebar_hider",
    version="0.0.1",
    description="Custom App to Hide Sidebar in ERPNext",
    author="Your Company",
    author_email="support@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"]
)
