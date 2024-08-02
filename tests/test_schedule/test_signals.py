import pytest
from model_bakery import baker

from repetitor.schedule.models import Schedule


@pytest.mark.db
def test_schedule_signals(django_user_model):
    assert not Schedule.objects.all().exists()

    user = baker.make(django_user_model)

    assert isinstance(user.schedule, Schedule)
    assert Schedule.objects.all().count() == 1

    user.save()
    assert Schedule.objects.all().count() == 1
