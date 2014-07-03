# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from config.tmpl_middleware import TemplateResponse
from tekton import router
from web.login import passwordless, facebook
from web.permission import home as permission_home, admin


@login_required
@no_csrf
def index():
    return TemplateResponse({'security_table_path': router.to_path(permission_home.index),
                             'permission_admin_path': router.to_path(admin),
                             'passwordless_admin_path': router.to_path(passwordless.form),
                             'facebook_admin_path': router.to_path(facebook.form)})
