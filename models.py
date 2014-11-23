from django.db.models import DateField, CharField, TextField, IntegerField, ForeignKey, Model, URLField


class TimeLineEvent(Model):
    group = CharField(max_length=30, blank=True)
    start = DateField()
    start_resolution = IntegerField(default=0)
    end = DateField(null=True, blank=True)
    end_resolution = IntegerField(default=0)
    title = CharField(max_length=1000)
    description = TextField(blank=True)

    def __unicode__(self):
        return self.title


class Url(Model):
    event = ForeignKey(TimeLineEvent, related_name='urls')
    order = IntegerField(default=1)
    url = URLField()

    def __unicode__(self):
        return self.url
