import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os

class OdnThemePlugin(plugins.SingletonPlugin):
    '''An comsode theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        config['ckan.site_logo'] = '/base/images/odnlogo.png'     
        config['ckan.favicon'] = '/base/images/odnicon.ico'     
        config['ckan.site_title'] = 'COMSODE - Open Data Node'
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        
		