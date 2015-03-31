import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as h
import os
from ckan.lib.app_globals import auto_update

auto_update.append('ckan.odn_version')

def localized_url_for_static(link):
    return h.url_for_static("{lang}/{link}".format(lang=h.lang(), link=link))

class OdnThemePlugin(plugins.SingletonPlugin):
    '''An comsode theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_public_directory(config, '../i18n')
    
    def get_helpers(self):
        return {'localized_url_for_static': localized_url_for_static}
