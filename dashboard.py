"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'rumbacaracas.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.LinkList(
            title='Quick Links',
            layout='inline',
            column=1,
            children = (
                {
                    'title':_('Legacy E-Rumba System'),
                    'url': 'http://erumba.rumbacaracas.com',
                    'external': True,
                },
                {
                    'title':_('E-Rumba Generation Tool'),
                    'url': '/e-rumba/setup/',
                    'external': True,
                },
                {
                    'title':_('Legacy People Upload'),
                    'url': 'http://old.rumbacaracas.com/ftp/',
                    'external': True,
                },
                {
                    'title':_('Legacy People Cropper'),
                    'url': 'http://old.rumbacaracas.com/cropear/',
                    'external': True,
                },
            )
        ))
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('AppList: Applications'),
            collapsible=True,
            column=1,
            exclude=('django.contrib.*',),
        ))
        
        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('ModelList: Administration'),
            column=1,
            collapsible=True,
            models=('django.contrib.*',),
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))


