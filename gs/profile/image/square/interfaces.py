# -*- coding: utf-8 -*-
from zope.schema import ASCIILine, Int
from gs.profile.image.base.interfaces import IGSUserImage


class IGSSquareUserImage(IGSUserImage):
    """A Square User Image"""

    size = Int(
        title=u'Size',
        description=u'The width and height of the image, in pixels.',
        required=False,
        default=50)  # FIXME: use gs.config

    missingImage = ASCIILine(
        title=u'Missing Image',
        description=u'The URL of the image to use for the missing-image '
                    u'image.',
        required=False,
        default='/++resource++gs-profile-image-base-missing.jpg')
