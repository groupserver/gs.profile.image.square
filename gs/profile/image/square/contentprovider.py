# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from userimage import SquareUserImage
from gs.profile.image.base.contentprovider import UserImageContentProvider


class SquareUserImageContentProvider(UserImageContentProvider):
    """The square user image."""
    def __init__(self, context, request, view):
        super(SquareUserImageContentProvider, self).__init__(context, request,
                                                                view)

    def update(self):
        super(SquareUserImageContentProvider, self).update()
        self.pageTemplate = PageTemplateFile(self.pageTemplateFileName)

    def get_final_size(self):
        if self.showMissingImage:
            retval = [int(d) for d in (self.size, self.size)]
        elif self.resizeNeeded:
            retval = self.smallImage.getImageSize()
        else:
            retval = self.userImage.getImageSize()
        return retval

    @Lazy
    def userImage(self):
        retval = SquareUserImage(self.context, self.userInfo)
        return retval

    @Lazy
    def resizeNeeded(self):
        retval = (int(self.size) != self.userImage.width
                    != self.userImage.height)
        return retval

    @Lazy
    def smallImage(self):
        if self.resizeNeeded:
            retval = self.userImage.get_resized(int(self.size))
        else:
            retval = self.userImage
        return retval

    def profile_image_link(self):
        r = '{profile}/gs-profile-image-square'
        retval = r.format(profile=self.userInfo.url)
        return retval

    def resize_link(self):
        r = '{profileLink}/{size}'
        return r.format(profileLink=self.profile_image_link(), size=self.size)
