from django.db import models

class T_ticket(models.Model):
    ticket_id = models.CharField(max_length=10,primary_key=True)
    channel = models.CharField(max_length=50,blank=True,null=True)
    user_uin = models.CharField(max_length=12,null=True,blank=True)
    own_uin = models.CharField(max_length=12,blank=True,null=True)
    own_name = models.CharField(max_length=50,blank=True,null=True)

    own_phone = models.CharField(max_length=15,blank=True,null=True)
    user_type = models.CharField(max_length=50,blank=True,null=True)
    service_combination = models.CharField(max_length=50,blank=True,null=True)
    service = models.CharField(max_length=50,blank=True,null=True)
    service_situation = models.CharField(max_length=50,blank=True,null=True)
    
    label_one = models.CharField(max_length=50,blank=True,null=True)
    label_two = models.CharField(max_length=50,blank=True,null=True)
    label_Three = models.CharField(max_length=50,blank=True,null=True)
    question = models.TextField(blank=True,null=True)
    answer = models.TextField(blank=True,null=True)

    effect_level = models.CharField(max_length=10,blank=True,null=True)
    functional_correlation = models.CharField(max_length=50,blank=True)
    handel_person = models.CharField(max_length=50,blank=True,null=True)
    team = models.CharField(max_length=50,blank=True,null=True)
    level = models.CharField(max_length=50,blank=True,null=True)

    start_time = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    queue_time = models.CharField(max_length=10,blank=True,null=True)
    response_time = models.CharField(max_length=10,blank=True,null=True)
    total_time = models.CharField(max_length=10,blank=True,null=True)
    levelone_t = models.CharField(max_length=10,blank=True,null=True)
    
    leveltwo_t = models.CharField(max_length=10,blank=True,null=True)
    levelthree_t = models.CharField(max_length=10,blank=True,null=True)
    levelFore_t = models.CharField(max_length=10,blank=True,null=True)
    customer_evaluation = models.CharField(max_length=10,blank=True,null=True)
    ticket_ctime = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)

    session_id = models.CharField(max_length=15,blank=True,null=True)
    job_number = models.CharField(max_length=15,blank=True,null=True)
    ticket_status = models.CharField(max_length=15,blank=True,null=True)
    tosb = models.CharField(max_length=15,blank=True,null=True)
    is_solved = models.CharField(max_length=15,blank=True,null=True)

    comment = models.TextField(blank=True,null=True)

    def __unicode_(self):
        return self.ticket_id
