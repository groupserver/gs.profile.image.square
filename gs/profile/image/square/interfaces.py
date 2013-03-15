# -*- coding: utf-8 -*-
from zope.schema import ASCIILine, Int
from gs.profile.image.base.interfaces import IGSUserImage


class IGSSquareUserImage(IGSUserImage):
    """A Square User Image"""
    pageTemplateFileName = ASCIILine(
        title=u"Page Template File Name",
        description=u'The name of the ZPT file that is used to render the '
                    u'profile image.',
        required=False,
        default="browser/templates/userimage.pt")

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
        default='/++resource++gs-profile-image-square-missing.jpg')
