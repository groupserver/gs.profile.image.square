# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.profile.image.square',
    version=version,
    description="Support for square profile images in GroupServer.",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='profile image content provider',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.profile', 'gs.profile.image'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.browserresource',
        'zope.cachedescriptors',
        'zope.contentprovider',
        'zope.pagetemplate',
        'zope.publisher',
        'zope.schema',
        'gs.image',
        'gs.profile.base',
        'gs.viewlet',
        'Products.CustomUserFolder',
        'Products.XWFCore',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
