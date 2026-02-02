"""
Setup configuration for the binarytree package.
"""

from setuptools import setup, find_packages

setup(
    name="binarytree-cfd",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive binary tree implementation with YAML integration",
    url="https://github.com/yourusername/binarytree-package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyYAML>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "mypy>=1.0",
            "flake8>=6.0",
        ],
    },
    keywords="binary-tree data-structures yaml tree algorithms",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/binarytree-package/issues",
        "Source": "https://github.com/yourusername/binarytree-package",
    },
)