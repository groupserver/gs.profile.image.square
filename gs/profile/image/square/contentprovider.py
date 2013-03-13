# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from userimage import SquareUserImage
from gs.profile.image.base.contentprovider import UserImageContentProvider


class SquareUserImageContentProvider(UserImageContentProvider):
    """GroupServer view of the user image
    """
    def __init__(self, context, request, view):
        super(SquareUserImageContentProvider, self).__init__(context, request,
                                                                view)
        self.__updated = False

    def update(self):
        self.__updated = True
        self.pageTemplate = PageTemplateFile(self.pageTemplateFileName)

    def render(self):
        if not self.__updated:
            raise UpdateNotCalled
        return self.pageTemplate(view=self)

    @Lazy
    def userImage(self):
        retval = SquareUserImage(self.context, self.userInfo)
        return retval

    @Lazy
    def userImageUrl(self):
        retval = self.missingImage
        try:
            if (not(self.userInfo.anonymous) and self.userImage.imagePath):
                r = '{profile}/gs-profile-image-square/{size}'
                retval = r.format(profile=self.userInfo.url, size=self.size)
        except IOError:
            pass  # Use the missingImage
        return retval
