from setuptools import find_packages, setup

setup(
    name="apixdev",
    version="0.1.2",
    description="Apix Developper Toolkit",
    keywords="apix docker odoo development",
    url="https://gitlab.apik.cloud/dev/apixdev",
    author="Aurelien ROY",
    author_email="roy.aurelien@gmail.com",
    license="MIT",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
    # python_requires='>=3.8',
    install_requires=[
        "click",
        "gitdb",
        "GitPython",
        "OdooRPC",
        "python-gitlab",
        "PyYAML>=6.0",
        "requests",
        "sh",
        "tqdm",
        "requirements-parser",
    ],
    entry_points={
        "console_scripts": [
            "apix = apixdev.cli.main:cli",
        ],
    },
)