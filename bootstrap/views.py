from django.shortcuts import render_to_response  
#中文测试
from django.template import RequestContext  
from django.http import HttpResponseRedirect,HttpResponse 
from django.core.urlresolvers import reverse  

import pyexcel.ext.xls
import django_excel
import pyexcel.ext.xlsx
import pyexcel
from .models import Document  
from .model.t_Ticket import T_ticket
from .forms.addFile import DocumentForm  
from .forms.addName import NameForm
from .forms.regUser import RegUser
from .models import User
from .forms.addFile import ExcelForm 
from .model.t_Question import Question
from .model.t_Question import Choice
def list(request):  
    # Handle file upload  
    if request.method == 'POST':  
        form = DocumentForm(request.POST, request.FILES)  
        if form.is_valid():  
            newdoc = Document(docfile = request.FILES['docfile'])  
            newdoc.save()  
  
            # Redirect to the document list after POST  
            return HttpResponseRedirect(reverse('bootstrap:list'))  
    else:  
        form = DocumentForm() # A empty, unbound form  
  
    # Load documents for the list page  
    documents = Document.objects.all()  
  
    # Render list page with the documents and the form  
    return render_to_response(  
        'bootstrap/list.html',  
        {'documents': documents, 'form': form},  
        context_instance=RequestContext(request)  
    )  

def regist(req):
    if req.method =='POST':
        uf = RegUser(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username,password=password)
            f = open('/data/dennie/pythontest/lib/python3.5/site-packages/django/bin/mysite/media/documents/2016/03/a.txt',encoding="utf-8")
            TickList = []
            for line in f:
                (ticket_id, channel, user_uin , own_uin, own_name, own_phone,
                user_type, service_combination, service, service_situation,
                label_one, label_two, label_Three, question, answer, effect_level,
                functional_correlation, handel_person, team, level, start_time,
                queue_time, response_time, total_time, levelone_t, leveltwo_t,
                levelthree_t, levelFore_t, customer_evaluation, ticket_ctime,
                session_id, job_number, ticket_status, tosb, is_solved, comment) = line.split(',')
                ticket = T_ticket(ticket_id=ticket_id, channel=channel,
                             user_uin=user_uin , own_uin=own_uin,
                             own_name=own_name, own_phone=own_phone,
                             user_type=user_type,
                             service_combination=service_combination,
                             service=service,
                             service_situation=service_situation,
                             label_one=label_one, label_two=label_two,
                             label_Three=label_Three, question=question,
                             answer=answer, effect_level=effect_level,
                             functional_correlation=functional_correlation,
                             handel_person=handel_person, team=team,
                             level=level, start_time=start_time,
                             queue_time=queue_time,
                             response_time=response_time,
                             total_time=total_time, levelone_t=levelone_t,
                             leveltwo_t=levelthree_t,
                             levelthree_t=levelthree_t,
                             levelFore_t=levelFore_t,
                             customer_evaluation=customer_evaluation,
                             ticket_ctime=ticket_ctime, session_id=session_id,
                             job_number=job_number,
                             ticket_status=ticket_status, tosb=tosb,
                             is_solved=is_solved, comment=comment
                             )

                TickList.append(ticket)
            f.close()

            T_ticket.objects.bulk_create(TickList)
            #T_ticket.objects.create(ticket_id=554536,user_uin=123456789)
            return HttpResponse('regist success')
    else:
        uf = RegUser()
    return render_to_response(
        'bootstrap/register.html',
        {'uf': uf},
        context_instance=RequestContext(req),
     )


def login(req):
    if req.method == 'POST':
        uf = RegUser(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user=User.objects.filter(username__exact = username,password__exact
                                     = password)
            if user:
                response = HttpResponseRedirect('/bootstrap/index')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/bootstrap/login')
    else:
        uf = RegUser()
    return render_to_response(
        'bootstrap/login.html',
        {'uf':uf},
        context_instance=RequestContext(req)
    )

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response(
        'bootstrap/index.html',
        {'username':username}
    )


def logout(req):
    #response = HttpResponse('logout!!')
    # response.delete_cookie('usename')
    #uf = RegUser()
    #return render_to_response(
    #    'bootstrap/login.html',
    #    {'uf':uf},
    #    context_instance=RequestContext(req),
    #    'bootstrap/index.html',¬
    #     {'username':username}¬

    # )
   response = HttpResponseRedirect('/bootstrap/index')
   response.delete_cookie('username')
   return response


def uploadExcel(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST,request.FILES)
        if form.is_valid():
            filehandle = request.FILES['excelfile']
            return django_excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download" )
    else:
        form = ExcelForm()
    return render_to_response("bootstrap/upload_form.html",
        {'form':form}, context_instance=RequestContext(request)
    )

def importdb(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        def choice_func(row):
            q=Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['excelfile'].save_book_to_database(
                models=[Question, Choice],
                initializers=[None, choice_func],
                mapdicts=[
                    ['question_text', 'pub_date', 'slug'],
                    ['question', 'choice_text', 'votes']]
            )

            return HttpResponse('ok', status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = ExcelForm()
    return render_to_response("bootstrap/upload_db.html", {'form':form},
        context_instance=RequestContext(request),
         )

def import_sheet(request):
    if request.method == "POST":
        form = ExcelForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            request.FILES['excelfile'].save_to_database(
                name_columns_by_row=2,
                model=Question,
                mapdict=['question_text', 'pub_date', 'slug'])
            '''
                mapdict={"Question Text": "question_text",
                           "Publish Date": "pub_date",
                         "测试": "slug"}
            )
            '''
            return HttpResponse("OK",status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = ExcelForm()
    return render_to_response('bootstrap/sheet_db.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def import_safe(request):
    if request.method == "POST":
        form = ExcelForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['excelfile'].save_to_database(
                name_columns_by_row=0,
                model=T_ticket,
                mapdict=['ticket_id', 'channel', 'user_uin', 'own_uin', 'own_name', 
				'own_phone','user_type', 'service_combination', 'service', 
				'service_situation', 'label_one', 'label_two', 'label_Three', 'question',
				'answer', 'effect_level', 'functional_correlation', 'handel_person', 'team',
				'level', 'start_time','queue_time', 'response_time', 'total_time', 
				'levelone_t', 'leveltwo_t','levelthree_t', 'levelFore_t', 'customer_evaluation', 
				'ticket_ctime', 'session_id', 'job_number', 'ticket_status', 'tosb',
				'is_solved', 'comment'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = ExcelForm()
    return render_to_response('bootstrap/sheet_safe.html',
                              {'form': form},
                              context_instance=RequestContext(request))




