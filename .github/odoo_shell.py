_logger = odoo.api.logging.getLogger("Github")
_logger.info("=== Install modules ===")
modules = [
    'contact',
    'sale_management',
]
modules = env['ir.module.module'].search([('name','in',modules),('state','=','uninstalled')])
for module in modules:
    _logger.info("Install %s" % (module.name))
    module.button_immediate_install()

_logger.info("--- Install modules ---")