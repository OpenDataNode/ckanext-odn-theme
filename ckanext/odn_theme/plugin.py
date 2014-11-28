import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os

class OdnThemePlugin(plugins.SingletonPlugin):
    '''An comsode theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        config['ckan.site_logo'] = '/images/odnlogo.png'     
        config['ckan.site_custom_css'] = '/images/comsode_theme.css'     
        
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        
		