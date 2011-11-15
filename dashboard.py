"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'rumbacaracas.dashboard.CustomIndexDashboard'
"""
from django.template.defaultfilters import capfirst

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.modules import DashboardModule
from grappelli.dashboard.utils import get_admin_site_name
from zinnia.models import Entry
from events.models import Event
from locations.models import Location
from yourphotos.models import Photo
from yourvideos.models import Video


class NewContent(DashboardModule):
    """
    Module that lists not proccessed content.
    """
    title = _('Pending content')
    template = 'main/admin_pending_content.html'
    limit = 10
    include_list = None
    exclude_list = None

    def __init__(self, title=None, limit=10, include_list=None,
                 exclude_list=None, **kwargs):
        self.include_list = include_list or []
        self.exclude_list = exclude_list or []
        kwargs.update({'limit': limit})
        super(NewContent, self).__init__(title, **kwargs)

    def init_with_context(self, context):
        if self._initialized:
            return
        from django.db.models import Q
        from django.contrib.admin.models import LogEntry

        request = context['request']

        tracked = (
            Photo,
            Event,
            Entry,
            Location,
            Video,
        )

        for model in tracked:
            app_label = model._meta.app_label
            not_published = '2'
            if app_label == 'zinnia':
                not_published = '0'

            self.children.append(
                {
                    'title': capfirst(app_label.title())+ ' - ' + model._meta.verbose_name.title(),
                    'url': reverse('%s:%s_%s_changelist' % (get_admin_site_name(context),app_label,model.__name__.lower())) + '?status__exact='+not_published,
                    'count': len(model.objects.filter(status__exact=not_published))
                }
            )

        if not len(self.children):
            self.pre_content = _('No pending content.')
        self._initialized = True

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
        
        self.children.append(NewContent(
            title=_('User pending content'),
            column=2,
            limit=5,
        ))


