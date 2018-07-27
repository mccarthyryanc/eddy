from setuptools import setup, find_packages

print('PACKAGES: ',find_packages())

setup(name='eddy',
      version='0.1',
      description='Simple, threaded, progress spinner',
      classifiers=[
        'Programming Language :: Python :: 3.6',
      ],
      keywords='time progress threading',
      author='Ryan McCarthy',
      author_email='ryan@mcginger.net',
      license='MIT',
      package_dir={'': '.'},
      packages=find_packages(),
      # entry_points='''
      #   [console_scripts]
      #   cli=eddy.eddycli.eddycli:cli
      # ''',
      include_package_data=True,
      zip_safe=False)