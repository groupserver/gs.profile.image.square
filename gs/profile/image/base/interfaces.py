# coding=utf-8
from zope.contentprovider.interfaces import IContentProvider
from zope.schema import ASCIILine, Field, Bool


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
