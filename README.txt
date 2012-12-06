Introduction
============

This product supplies the core code for displaying profile images. It
provides a `content provider`_, a page_ and a resource_.

Content Provider
================

The ``groupserver.UserImage`` content provider is used by almost all the
code that needs to display a profile image::

  <div tal:define="user view/userInstanceToShow"
       tal:replace="structure provider:groupserver.UserImage" />

It returns a ``<div>`` element (with the ``userimage`` and ``photo``
classes) that contains an ``<image>`` element.

Page
====

The ``gs-profile-image`` "page" is a view that returns the image for the
user. If there is no image the viewer is redirected to the resource_
instead.

Resource
========

The resource ``/++resource++gs-profile-image-base-missing.jpg`` is the
*missing profile image* image.


Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.profile.image.base
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver
