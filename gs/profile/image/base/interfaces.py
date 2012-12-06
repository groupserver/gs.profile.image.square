# coding=utf-8
from zope.contentprovider.interfaces import IContentProvider
from zope.schema import ASCIILine, Bool, Field, Int


class IGSUserImage(IContentProvider):
    """User Image"""
    pageTemplateFileName = ASCIILine(
        title=u"Page Template File Name",
        description=u'The name of the ZPT file that is used to render the '
                    u'profile image.',
        required=False,
        default="browser/templates/userimage.pt")

    user = Field(
        title=u'User Instance',
        description=u'An instance of the CustomUser Class',
        required=True)

    showImageRegardlessOfUserSetting = Bool(
        title=u'Show Image Regardles of User Setting',
        description=u"Show the user's image, regardless of the value of "
                    u"the showImage property. This should be used with "
                    u"extreme caution, as it can violate the user's privacy.",
        required=False,
        default=False)

    width = Int(
        title=u'Width',
        description=u'The width of the image, in pixels.',
        required=False,
        default=54)  # FIXME: use gs.config

    height = Int(
        title=u'Height',
        description=u'The height of the image, in pixels.',
        required=False,
        default=72)  # FIXME: use gs.config

    missingImage = ASCIILine(
        title=u'Missing Image',
        description=u'The URL of the image to use for the missing-image '
                    u'image.',
        required=False,
        default='/++resource++gs-profile-image-base-missing.jpg')
