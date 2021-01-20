import json
from kombu import Exchange
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from olympus.schemas import DataChangeEvent
from ... import models
from ...schemas import response
from . import connection


users = Exchange(
    name='olymp.access.users',
    type='topic',
    durable=True,
    channel=connection.channel(),
    delivery_mode=Exchange.PERSISTENT_DELIVERY_MODE,
)
users.declare()


@receiver(post_save, sender=models.User)
def post_save_user(sender, instance: models.User, created: bool, **kwargs):
    action = 'create' if created else 'update'
    data = async_to_sync(response.User.from_orm)(instance, tenant=None)
    body = DataChangeEvent(
        data=data,
        data_type='access.user',
        data_op=getattr(DataChangeEvent.DataOperation, action.upper()),
    )
    connection.ensure(users, users.publish)(
        message=body.json(),
        routing_key=f'v1.data.{action}',
    )


@receiver(post_delete, sender=models.User)
def post_delete_user(sender, instance: models.User, **kwargs):
    body = DataChangeEvent(
        data={
            'id': instance.id,
        },
        data_type='access.user',
        data_op=DataChangeEvent.DataOperation.DELETE,
    )
    connection.ensure(users, users.publish)(
        message=body.json(),
        routing_key='v1.data.delete',
    )
