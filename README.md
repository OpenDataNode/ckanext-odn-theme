ckanext-odn-theme
-------

ODN theme for CKAN

Plugin for extending package extras view.

Installation
-------

To enable plugin, change property in your production.ini:
```
ckan.plugins = odn_theme odn_package_extras
```

set in .ini:
* ckan.site_title = COMSODE - Open Data Node 
* ckan.site_logo = /base/images/odnlogo.png

Restart of apache AS is required: ``` service apache2 restart ```

Licenses
-------

Dual licensing is used for ODN theme.
* Code unde [GNU Affero General Public License, Version 3.0](http://www.gnu.org/licenses/agpl-3.0.html) (see LICENSE.code)
* Artwork under [Create Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode) (see LICENSE.artwork)
