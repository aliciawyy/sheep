from setuptools import setup


setup(
    name="sheepts",
    version="0.0.1",
    description="Light Time Series Toolbox",
    url="https://github.com/aliciawyy/sheep",
    author=["Alice Wang"],
    author_email="rainingilove@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License"
        ],
    install_requires=["pandas"],
    keywords="pandas time-series toolbox",
    packages=["sheepts"],
)
