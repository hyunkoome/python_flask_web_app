import setuptools

with open("requirements.txt", 'r') as requirements_file:
    requirements_list = requirements_file.read().splitlines()

setuptools.setup(
    name="hyunkookim",
    version="0.0.1",
    author="HyunKoo Kim",
    author_email="hyunkookim.me@gmail.com",
    description="python flask web app",
    python_requires='>=3.10.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=requirements_list,
)
