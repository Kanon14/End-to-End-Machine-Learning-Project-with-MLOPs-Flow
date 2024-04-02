import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    

__version__ ="0.0.0"

REPO_NAME = "End-to-End-Machine-Learning-Project-with-MLOPs-Flow"
AUTHOR_USER_NAME = "Kanon14"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "geochua144@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
    
    