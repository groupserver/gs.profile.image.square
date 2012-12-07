# -*- coding: utf-8 -*-
from errno import ENOENT
from glob import glob
import os.path
from zope.cachedescriptors.property import Lazy
from gs.image import GSImage
from Products.XWFCore.XWFUtils import locateDataDirectory


class UserImage(GSImage):

    def __init__(self, context, userInfo):
        assert context
        self.context = context

        assert userInfo
        self.userInfo = userInfo

        super(UserImage, self).__init__(self.file)

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
        else:
            m = 'Cannot open the profile image for {name} ({id})'
            msg = m.format(name=self.userInfo.name, id=self.userInfo.id)
            raise IOError(ENOENT, msg, imagePath)
        return retval

    @Lazy
    def file(self):
        retval = None

        if self.imagePath:
            retval = file(self.imagePath, 'rb')
        return retval
