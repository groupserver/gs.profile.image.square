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
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from gs.core import to_ascii
from gs.profile.image.base import Image
from .userimage import SquareUserImage


class SquareImage(Image):

    def __init__(self, context, request):
        super(SquareImage, self).__init__(context, request)

    @Lazy
    def userImage(self):
        retval = SquareUserImage(self.context, self.userInfo)
        return retval

    @Lazy
    def size(self):
        tsp = self.traverse_subpath
        if len(tsp) > 0:
            retval = int(tsp[0])
        else:
            retval = self.userImage.width
        return retval

    @Lazy
    def image(self):
        if self.userImage.width == self.userImage.height == self.size:
            retval = self.userImage
        else:
            retval = self.userImage.get_resized(self.size)
        return retval

    def __call__(self):
        # TODO: Add the x-sendfile suff
        try:
            h = 'inline; filename={0}-square-{1}.jpg'
            hdr = h.format(self.userInfo.nickname, self.size)
            self.request.RESPONSE.setHeader(to_ascii('Content-Disposition'),
                                            to_ascii(hdr))

            self.request.RESPONSE.setHeader(to_ascii('Cache-Control'),
                                            to_ascii('private; max-age=1200'))

            self.request.RESPONSE.setHeader(to_ascii('Content-Length'),
                                            to_ascii(str(self.image.getSize())))

            self.request.RESPONSE.setHeader(to_ascii('Content-Type'),
                                            to_ascii(self.image.contentType))
            retval = self.image.data
        except IOError:
            missingImage = '/++resource++gs-profile-image-square-missing.jpg'
            retval = self.request.RESPONSE.redirect(missingImage)
        return retval
