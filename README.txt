===========================
``gs.profile.image.square``
===========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Square profile images for GroupServer Users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_,
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-14
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product supplies the code for displaying square profile images. It is
based on ``gs.profile.image.base`` [#base]_, but uses the
``gs.image.GSSquare`` class to do the resizing and cropping [#image]_. 

The `content provider`_ supplied by this class is used to add images to
pages. It calls the view_ if the image exists, or links to the `missing
image`_ resource if it does not.

Content Provider
================

The ``groupserver.SquareUserImage`` content provider is used by almost all
the code that needs to display a profile image::

  <div tal:define="user view/userInstanceToShow"
       tal:replace="structure provider:groupserver.SquareUserImage" />

The optional ``size`` argument can be passed to the content provider to
change the dimensions of the image::

  <div tal:define="user view/userInstanceToShow; size string:40"
       tal:replace="structure provider:groupserver.SquareUserImage" />


Otherwise the output is the same as for the base code [#base]_.

View
====

The view ``/p/{userId}/gs-profile-image-square`` is a view that returns the
image for the user. One optional arguments can be passed as part of a path,
to set the width and the height of the image.

* Not providing any arguments displays the **original** image, cropped so
  the longest side is equal in length to the shortest side:
  <http://groupserver.org/p/mpj17/gs-profile-image-square>.

* If an argument is provided, then the image is scaled so the shortest side
  is equal to the given length, and the other side unconstrained. Then the
  longest side is cropped to the given length, resulting in a square image:
  <http://groupserver.org/p/mpj17/gs-profile-image-square/100>.

Missing Image
=============

The resource ``/++resource++gs-profile-image-square-missing.jpg`` is the
*missing profile image* image.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.profile.image.square
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17/
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#base] See <https://source.iopen.net/groupserver/gs.profile.image.base>
.. [#image] See <https://source.iopen.net/groupserver/gs.image>

..  LocalWords:  groupserver
