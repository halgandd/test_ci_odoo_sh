_logger = odoo.api.logging.getLogger("Github")
_logger.info("=== Install translations ===")
translations = [
    'fr_FR',
]
langs = env['res.lang'].with_context(active_test=False).search_read([('code', 'in', translations)], ['code', 'active'])
for translation in translations:
    for lang in langs:
        if lang['code'] == translation:
            if lang['active']:
                _logger.info("\t- Translation %s already installed" % translation)
            else:
                _logger.info("\t- Install %s Translation" % translation)
                wizard_id = env['base.language.install'].create({'lang': translation})
                wizard_id.lang_install()

_logger.info("--- Translations installed ---")