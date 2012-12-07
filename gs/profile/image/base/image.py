# -*- coding: utf-8 -*-
from glob import glob
import os.path
from zope.cachedescriptors.property import Lazy
from Products.XWFCore.XWFUtils import locateDataDirectory
from gs.image import GSImage
from gs.profile.base.page import ProfilePage


class Image(ProfilePage):

    def __init__(self, context, request):
        super(Image, self).__init__(context, request)
        self.traverse_subpath = []

    def publishTraverse(self, request, name):
        self.traverse_subpath.append(name)
        return self

    @Lazy
    def imageDir(self):
        # TODO: Cache
        site_root = self.context.site_root()
        siteId = site_root.getId()
        retval = locateDataDirectory("groupserver.user.image", (siteId,))
        return retval

    @Lazy
    def imagePath(self):
        # TODO: Cache
        # --=mpj17=-- Note to Future Coder: version numbers could be added to
        # the files: something like userId-YYYYMMDDHHMMSS.ext ?
        # '{0}-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
        # '[0-9][0-9].*'.format(self.userInfo.id)
        filename = '{0}.*'.format(self.userInfo.id)
        imagePath = os.path.join(self.imageDir, filename)

        retval = None
        files = glob(imagePath)
        if files and os.path.isfile(files[0]):
            retval = files[0]
        return retval

    @Lazy
    def width(self):
        tsp = self.traverse_subpath
        if len(tsp) > 0:
            retval = int(tsp[0])
        else:
            retval = 54  # FIXME: use gs.config
        return retval

    @Lazy
    def height(self):
        tsp = self.traverse_subpath
        if len(tsp) >= 2:
            retval = int(tsp[1])
        else:
            retval = 72  # FIXME: use gs.config
        return retval

    @Lazy
    def image(self):
        retval = None
        if self.imagePath:
            f = file(self.imagePath, 'rb')
            gsImage = GSImage(f)
            retval = gsImage.get_resized(self.width, self.height,
                                            maintain_aspect=True)
        return retval

    def __call__(self):
        # TODO: Add the x-sendfile suff
        if self.image:
            hdr = 'inline; filename={0}.jpg'.format(self.userInfo.id)
            self.request.RESPONSE.setHeader('Content-Disposition', hdr)

            self.request.RESPONSE.setHeader('Cache-Control',
                                            'private; max-age=1200')

            self.request.RESPONSE.setHeader('Content-Type',
                                            self.image.contentType)
            retval = self.image.data
        else:
            missingImage = '/++resource++gs-profile-image-base-missing.jpg'
            retval = self.request.RESPONSE.redirect(missingImage)
        return retval
