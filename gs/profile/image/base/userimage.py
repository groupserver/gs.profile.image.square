# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from zope.interface import implements, Interface
from zope.component import adapts, createObject, provideAdapter
from zope.contentprovider.interfaces import UpdateNotCalled, IContentProvider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from gs.viewlet.contentprovider import SiteContentProvider
from Products.XWFCore import XWFUtils
from interfaces import IGSUserImage


class UserImageContentProvider(SiteContentProvider):
    """GroupServer view of the user image
    """
    def __init__(self, context, request, view):
        super(UserImageContentProvider, self).__init__(context, request, view)
        self.__updated = False
        self.pageTemplate = None

    def update(self):
        self.__updated = True
        self.pageTemplate = PageTemplateFile(self.pageTemplateFileName)

    def render(self):
        if not self.__updated:
            raise UpdateNotCalled
        return self.pageTemplate(view=self)
        
    @Lazy
    def userImageUrl(self):
        # check that we aren't dealing with an Anonymous user
        if self.user.getId():
            retval = self.user.get_image() or ''
        else:
            retval = ''

        return retval
        
    @Lazy
    def userImageShow(self):
        retval = (bool(self.userImageUrl) 
                  and (self.showImageRegardlessOfUserSetting or
                       getattr(self.user, 'showImage', False)))
        assert type(retval) == bool
        return retval
