from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as buffer:
        content = buffer.read()
        requirements = content.split('\n')

    return requirements

setup(
    name="anime-cli-br",
    version="1.0.0",
    author="TheLowRam",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        anime-cli-br=cli.animecli:main
    '''
)