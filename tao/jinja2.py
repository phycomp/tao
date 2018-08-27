from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils import translation
from jinja2 import PackageLoader, Environment 

def environment(**options):
    #env = Environment(**options)
    env = Environment(extensions=['jinja2.ext.i18n'], **options)
    env.globals.update({'static':staticfiles_storage.url, 'url':reverse, })
    env.install_gettext_translations(translation)
    #env.install_gettext_translations(translation)
    #Environment.install_gettext_translations(translation)
    return env
'''
translations = get_gettext_translations()
env = Environment(extensions=['jinja2.ext.i18n'])'extensions':['jinja2.ext.i18n'], 
env.install_gettext_translations(translations)
template = env.get_template('test.jinja.html')
page_next_app_table = template.render()
jinja_environment = Environment(loader=PackageLoader('website', 'templates'), extensions=['jinja2.ext.i18n'])
#from __future__ import absolute_import  # Python 2 only
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({ 'static': staticfiles_storage.url, 'url': reverse, })
    return env
'''
