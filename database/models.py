from tortoise.models import Model
from tortoise import fields


class MessageInfo(Model):
    id = fields.IntField(pk=True)
    data = fields.TextField()

    class Meta:
        table = "Income messages"
