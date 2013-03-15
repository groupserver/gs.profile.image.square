# -*- coding: utf-8 -*-
from base64 import b64encode
from zope.cachedescriptors.property import Lazy
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from userimage import SquareUserImage
from gs.profile.image.base.contentprovider import UserImageContentProvider


class SquareUserImageContentProvider(UserImageContentProvider):
    """The square user image."""

    def update(self):
        self.updated = True
        self.pageTemplate = PageTemplateFile(self.pageTemplateFileName)

    @Lazy
    def userImage(self):
        retval = SquareUserImage(self.context, self.userInfo)
        return retval

    @Lazy
    def userImageUrl(self):
        retval = self.missingImage  # From the interface
        try:
            if (not(self.userInfo.anonymous)
                and (self.userImage.file is not None)):
                if int(self.size) >= 40:
                    retval = self.profile_image_link()
                else:
                    retval = self.embedded_profile_image()
        except IOError:
            pass  # Use the missingImage
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