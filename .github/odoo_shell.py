print("Install modules")
modules = [
    'contact',
    'sale_management',
]
env['ir.module.module'].search([('name','in',modules),('state','=','uninstalled')]).button_immediate_install()