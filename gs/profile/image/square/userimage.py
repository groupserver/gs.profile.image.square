# -*- coding: utf-8 -*-
from gs.image import GSSquareImage
from gs.profile.image.base import UserImage


class SquareUserImage(GSSquareImage, UserImage):

    def __init__(self, context, userInfo):
        self.context = context
        self.userInfo = userInfo
        super(GSSquareImage, self).__init__(self.file)
