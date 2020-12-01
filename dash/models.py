from django.db import models

# Create your models here.

class Dash(models.Model):
#    circleGraph
#    lineGraph
#    barGraph
#    map
#    sidebar
#    customerFeed
#    staticCard
#    sideMenu
#    taskCard


###           initially bar graph is created
    label = models.CharField(max_length=120)
    value = models.CharField(max_length=120)

    def _str_(self):
        return self.label