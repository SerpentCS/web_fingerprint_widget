# -*- coding: utf-8 -*-

##############################################################################
#
#    Authors: Authors: Timothy Solomon. Copyright Spiraleye.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Fingerprint Widget',
    'version': '0.1',
    'category': 'Added functionality / Widgets',
    'description': """
Adds a fingerprint reader to login (You can register users in the Biometrics tab under Settings > Users)

can be used to verify partners or users: 
view:
  <field name="biometric" widget="biometric" nolabel="1" context="{'default_type': 'users','default_type_id':id}"  />
or for partners:
  context="{'default_type': 'partner','default_type_id':partner}"
""",
    'author': '',
    'website': '',
    'depends': ['base'],
    #'js' : [
    #    'static/src/js/web_fingerprint_widget.js',
    #],

    'qweb' : [
        'static/src/xml/web_fingerprint_widget.xml',
        'static/src/xml/auth_uareu.xml',
    ],
    'data' : [
        'biometric.xml',
        'user.xml',
        'views/fingerprint.xml',

    ],
    'installable': True,
    'active': False,
}
