'''
Created on 10.12.2014

@author: mvi
'''

import ckan.plugins as p
import ckan.plugins.toolkit as tk

labels = {
    "creator":"Creator",
    "dataset":"Dataset",
    "modified":"Modified",
    "source":"Source",
    "void#exampleResource":"Example resource",
    "void#sparqlEndpoint":"SPARQL resource"
}

def get_label(key):
    if key in labels.keys():
        return labels[key]
    else:
        return key

class PackageExtrasPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)
    
    
    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    
    def get_helpers(self):
        return {'get_label':get_label}