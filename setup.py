from setuptools import setup, find_packages

setup(
    name="bobflow",
    version="1.0.0",
    description="AI-powered developer workflow CLI — powered by IBM Bob",
    packages=find_packages(),
    install_requires=["click>=8.0.0"],
    entry_points={
        "console_scripts": [
            "bobflow=bobflow.cli:cli",
        ],
    },
)
