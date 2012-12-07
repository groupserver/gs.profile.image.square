# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from gs.profile.base.page import ProfilePage
from userimage import UserImage


class Image(ProfilePage):

    def __init__(self, context, request):
        super(Image, self).__init__(context, request)
        self.traverse_subpath = []

    def publishTraverse(self, request, name):
        self.traverse_subpath.append(name)
        return self

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
        userImage = UserImage(self.context, self.userInfo)
        if userImage.image:
            retval = userImage.image.get_resized(self.width, self.height,
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
