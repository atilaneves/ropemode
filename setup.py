extra_kwargs = {}
try:
    from setuptools import setup
    extra_kwargs['install_requires'] = ['rope_py3k >= 0.9.4']
except ImportError:
    from distutils.core import setup

import ropemode


classifiers = [
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Environment :: X11 Applications',
    'Environment :: Win32 (MS Windows)',
    'Environment :: MacOS X',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development']

setup(name='ropemode_py3k',
      version=ropemode.VERSION,
      description=ropemode.INFO,
      author='Atila Neves',
      author_email='atila.neves@gmail.com',
      url='https://github.com/atilaneves/ropemode',
      packages=['ropemode'],
      license='GNU GPL',
      classifiers=classifiers,
      requires=['rope_py3k (>= 0.9.4)'],
      **extra_kwargs
      )
