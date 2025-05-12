from setuptools import setup, find_packages

setup(
    name="mcts_poker_bot",
    version="0.1.0",
    packages=find_packages(where="."),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "poker-bot = scripts.cli:main",
        ],
    },
)
