from django.db import models
from django_extensions.db.models import TimeStampedModel

from .person import Person
from .group import Group


class Client(TimeStampedModel):
    person = models.OneToOneField(Person, blank=True, null=True, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.target}'
    
    def save(self, **kwargs):
        assert [self.person, self.group].count(None) == 1, "Only 'group' or 'person' should be set"
        return super().save(**kwargs)
    
    @property
    def target(self):
        if self.person_id is not None:  # type: ignore
            return self.person
        if self.group_id is not None:  # type: ignore
            return self.group
        raise AssertionError("Neither 'group' nor 'person' is set")
