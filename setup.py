from setuptools import setup

setup(
    name="helmet-mimic",
    version="0.2.0",
    description="Random Pathfinder 2E monster stat block generator from Archive of Nethys",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pbr80/helmet-mimic",
    py_modules=["pathfinder_MOTD"],
    scripts=["20-helmet-mimic"],
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.6",
)
