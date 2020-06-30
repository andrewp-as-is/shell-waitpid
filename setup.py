import setuptools

setuptools.setup(
    name='shell-waitpid',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/waitpid']
)
