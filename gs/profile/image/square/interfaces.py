# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals
from zope.schema import ASCIILine, Int
from gs.profile.image.base.interfaces import IGSUserImage


class IGSSquareUserImage(IGSUserImage):
    """A Square User Image"""
    pageTemplateFileName = ASCIILine(
        title="Page Template File Name",
        description='The name of the ZPT file that is used to render the '
                    'profile image.',
        required=False,
        default="browser/templates/userimage.pt".encode('ascii', 'ignore'))

    size = Int(
        title='Size',
        description='The width and height of the image, in pixels.',
        required=False,
        default=50)  # FIXME: use gs.config

    missingImage = ASCIILine(
        title='Missing Image',
        description='The URL of the image to use for the missing-image '
                    'image.',
        required=False,
        default='/++resource++gs-profile-image-square-missing.jpg'.encode('ascii', 'ignore'))
