from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(name='edge_logger',
      version='0.0.1',
      description='An edge device data logger.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MarcelRoux/edge_logger',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      author='Marcel',
      author_email='',
      license='MIT',
      package_dir={'': 'edge_logger'},
      packages=find_packages(where='edge_logger'),
      python_requires='>=3.6'
)
