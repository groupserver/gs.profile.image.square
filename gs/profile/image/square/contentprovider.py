# -*- coding: utf-8 -*-
from base64 import b64encode
from zope.cachedescriptors.property import Lazy
from userimage import SquareUserImage
from gs.profile.image.base.contentprovider import UserImageContentProvider


class SquareUserImageContentProvider(UserImageContentProvider):
    """GroupServer view of the user image
    """
    def __init__(self, context, request, view):
        super(SquareUserImageContentProvider, self).__init__(context, request,
                                                                view)

    @Lazy
    def userImage(self):
        retval = SquareUserImage(self.context, self.userInfo)
        return retval

    def profile_image_link(self):
        r = '{profile}/gs-profile-image-square/{size}'
        retval = r.format(profile=self.userInfo.url, size=self.size)
        return retval

    def embedded_profile_image(self):
        smallImage = self.userImage.get_resized(self.size)
        d = b64encode(smallImage.data)
        r = 'data:{mediatype};base64,{data}'
        retval = r.format(mediatype=smallImage.contentType, data=d)
        return retval
