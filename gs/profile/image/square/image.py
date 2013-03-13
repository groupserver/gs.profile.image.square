# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from gs.profile.image.base.image import Image
from userimage import SquareUserImage


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
        if self.traverse_subpath:
            retval = self.userImage.get_resized(self.size)
        else:
            retval = self.userImage
        return retval

    def __call__(self):
        # TODO: Add the x-sendfile suff
        try:
            h = 'inline; filename={0}-square-{1}.jpg'
            hdr = h.format(self.userInfo.id, self.size)
            self.request.RESPONSE.setHeader('Content-Disposition', hdr)

            self.request.RESPONSE.setHeader('Cache-Control',
                                            'private; max-age=1200')

            self.request.RESPONSE.setHeader('Content-Length',
                                            self.image.getSize())

            self.request.RESPONSE.setHeader('Content-Type',
                                            self.image.contentType)
            retval = self.image.data
        except IOError:
            missingImage = '/++resource++gs-profile-image-square-missing.jpg'
            retval = self.request.RESPONSE.redirect(missingImage)
        return retval
