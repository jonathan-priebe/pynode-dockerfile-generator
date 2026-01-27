from setuptools import setup, find_packages

setup(
    name='dockerfile-generator',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,  # Wichtig!
    package_data={
        'dockerfile_generator': ['templates/*.j2'],
    },
    install_requires=[
        'click>=8.1.7',
        'jinja2>=3.1.2',
    ],
    entry_points={
        'console_scripts': [
            'dockerfile-generator=dockerfile_generator.cli:cli',
        ],
    },
    python_requires='>=3.12',
)