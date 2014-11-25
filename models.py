from django.db.models import DateField, CharField, TextField, IntegerField, ForeignKey, Model, URLField, FloatField


class TimeLineEvent(Model):
    group = CharField(max_length=30, default='derivative', blank=False)
    start = DateField(default='2014-01-01')
    end = DateField(default='2014-01-03')
    title = CharField(max_length=100)
    description = TextField(blank=True)
    exchange_rate = FloatField(default=1.35, null=True)
    url = URLField()

    def __unicode__(self):
        return self.title


class Url(Model):
    event = ForeignKey(TimeLineEvent, related_name='urls')
    order = IntegerField(default=1)
    url = URLField()

    def __unicode__(self):
        return self.url
