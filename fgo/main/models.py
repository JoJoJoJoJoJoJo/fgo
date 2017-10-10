from django.db import models
# from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.conf import settings


class Servant(models.Model):
    SERVANT_CHOICES = (('S','Saber'),
                       ('A','Archer'),
                       ('L','Lancer'),
                       ('R','Rider'),
                       ('C','Caster'),
                       ('As','Assassin'),
                       ('B','Berserker'),
                       ('Sh','Shielder'),
                       ('Al','Alterego'),
                       ('M','MoomCancer'),
                       )
    name = models.CharField(max_length=20)
    classes = models.CharField(max_length=20,choices=SERVANT_CHOICES)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    nick = models.CharField(max_length=50)
    # phantasm = models.OneToOneField(Phantasm,related_name='servant')
    features = models.CharField(max_length=200)
    max_attack = models.IntegerField()
    max_hp = models.IntegerField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return u'servant：{},class：{}'.format(self.name,self.classes)

    @property
    def lvlup_items(self,lv=4):
            pass


class Item(models.Model):
    name = models.CharField(max_length=20)
    nick = models.CharField(max_length=40)
    maps = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name


class Phantasm(models.Model):
    name = models.CharField(max_length=200)
    servant = models.ForeignKey(Servant,related_name='phantasm')
    # level = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    desc = models.CharField(max_length=400)
    # 宝具类型
    p_type = models.CharField(max_length=200)
    #E~EX级
    quality = models.CharField(max_length=10, choices=settings.QUALITY_CHOICES)

    def __str__(self):
        return self.name



class Lvlup(models.Model):
    #第？次再临
    servant = models.ForeignKey(Servant,related_name='lvlup')
    times = models.IntegerField()
    # items = models.ManyToManyField(Item,through=LvlupItemAmount,blank=True,)
    # amount = models.BigIntegerField(blank=True,null=True)
    # items = models.ForeignKey(LvlupItemAmount,blank=True)

    def __str__(self):
        return '{} times upgrade for {}'.format(self.times,self.servant)


class LvlupItemAmount(models.Model):
    lvlup = models.ForeignKey(Lvlup,related_name='items')
    item = models.ForeignKey(Item)
    amount = models.BigIntegerField(default=0)


class Skill(models.Model):
    name = models.CharField(max_length=200)
    servant = models.ForeignKey(Servant,related_name='skills')
    quality = models.CharField(max_length=10,choices=settings.QUALITY_CHOICES)
    cd = models.IntegerField()
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return '{} of servant {}'.format(self.name,self.servant)


class SkillLevel(models.Model):
    servant = models.ForeignKey(Servant,related_name='skilllevel')
    level = models.PositiveIntegerField()

    def save(self,*args,**kwargs):
        #新创建并且等级为1则自动增加后面10个等级
        #用singal更好
        if not self.pk and self.level == 1:
            for i in range(2,11):
                SkillLevel.objects.create(servant=self.servant,level=i)
        super(SkillLevel,self).save(*args,**kwargs)

    def __str__(self):
        return 'lv.{} skill of {}'.format(self.level,self.servant)

class SkillDetail(models.Model):
    skill = models.ForeignKey(Skill,related_name='detail')
    level = models.PositiveIntegerField()
    rate_or_number = models.FloatField()
    # items = models.ManyToManyField(Item,related_name='skill',through=SkillItemAmount,blank=True,)
    # amount = models.BigIntegerField(blank=True,null=True)

    def __str__(self):
        return '{},{}'.format(self.skill,self.rate_or_number)


class SkillItemAmount(models.Model):
    skill = models.ForeignKey(SkillLevel,related_name='items')
    item = models.ForeignKey(Item)
    amount = models.BigIntegerField(default=0)


class NegativeSkill(models.Model):
    name= models.CharField(max_length=100)
    servant = models.ForeignKey(Servant,related_name='ng_skill')
    # rate_or_number = models.FloatField()
    quality = models.CharField(choices=settings.QUALITY_CHOICES,max_length=100)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return '{} of {}'.format(self.name,self.servant)


class PhantasmLevelDetail(models.Model):
    phantasm = models.ForeignKey(Phantasm,related_name='level_detail')
    level = models.IntegerField()
    rate_or_number = models.FloatField()


class PhantasmOcDetal(models.Model):
    phantasm = models.ForeignKey(Phantasm,related_name='oc_detail')
    oc = models.IntegerField()
    rate_or_number = models.FloatField()


