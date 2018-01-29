from __future__ import unicode_literals

from django.db import models
from foods.models import (
    Diet as food_diet
)
from system_user.models import (
    Diet as user_diet
)

optional = {
    'null': True,
    'blank': True
}


class RulesMembership(models.Model):
    """
        January 4, 2017 - Kwen
        The model where the rules that are needed for inferencing are made 
    """
    name_of_variable = models.CharField(max_length=255, default='')
    domain = models.CharField(max_length=255)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name_of_variable)

    class Meta:
        verbose_name = "Rule Membership"
        verbose_name_plural = "Rules Membership"


class Rules(models.Model):
    """
        January 4, 2017 - Kwen
        The model where the rules that are needed for inferencing are made 
    """
    if_food_sodium_content_is = models.ForeignKey(RulesMembership, related_name = 'if_food_sodium_content_is')
    and_user_sodium_requirement_is = models.ForeignKey(RulesMembership, related_name = 'and_user_sodium_requirement_is')
    then_percentage_is = models.DecimalField(("Then Percentage"),max_digits=5,decimal_places=2)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {}".format(self.if_food_sodium_content_is, self.and_user_sodium_requirement_is, self.then_percentage_is)

    class Meta:
        verbose_name = "Rule"
        verbose_name_plural = "Rules"


class WorkingMemory(models.Model):
    """
        January 4, 2017 - Kwen
        The model for the working memory
    """
    name = models.CharField(max_length=255)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Working Memory"
        verbose_name_plural = "Working Memory"
