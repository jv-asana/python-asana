from asana.paths.webhooks_webhook_gid.get import ApiForget
from asana.paths.webhooks_webhook_gid.put import ApiForput
from asana.paths.webhooks_webhook_gid.delete import ApiFordelete


class WebhooksWebhookGid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
