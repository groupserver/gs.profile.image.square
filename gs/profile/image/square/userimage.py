# -*- coding: utf-8 -*-
from gs.image import GSSquareImage
from gs.profile.image.base.userimage import get_file


class SquareUserImage(GSSquareImage):

    def __init__(self, context, userInfo):
        self.context = context
        self.userInfo = userInfo
        self.file = get_file(context, userInfo)
        super(SquareUserImage, self).__init__(self.file)
