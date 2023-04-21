from pylon.core.tools import web  # pylint: disable=E0611,E0401
from tools import auth, theme  # pylint: disable=E0401


class Slot:  # pylint: disable=E1101,R0903
    @web.slot('secrets_content')
    @auth.decorators.check_slot(["configuration.secrets"], 
                                access_denied_reply=theme.access_denied_part)
    def content(self, context, slot, payload):
        from pylon.core.tools import log
        log.info('slot: [%s], payload: %s', slot, payload)
        with context.app.app_context():
            return self.descriptor.render_template(
                'secrets/content.html'
            )

    @web.slot('secrets_scripts')
    @auth.decorators.check_slot(["configuration.secrets"])
    def scripts(self, context, slot, payload):
        from pylon.core.tools import log
        log.info('slot: [%s], payload: %s', slot, payload)
        with context.app.app_context():
            return self.descriptor.render_template(
                'secrets/scripts.html',
            )

    @web.slot('secrets_styles')
    @auth.decorators.check_slot(["configuration.secrets"])
    def styles(self, context, slot, payload):
        from pylon.core.tools import log
        log.info('slot: [%s], payload: %s', slot, payload)
        with context.app.app_context():
            return self.descriptor.render_template(
                'secrets/styles.html',
            )
