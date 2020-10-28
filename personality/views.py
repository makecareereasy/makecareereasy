import os
import pickle
import numpy as np
import pandas as pd

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .models import TestQuestion, TestChoice, PersonalityType, PersonalityQuestion
from .utils import clear_test_session

User = get_user_model()
classifer_base = os.path.join(settings.BASE_DIR, 'personality', 'classifiers')

class AptitudeTest(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.applicant.taken_apt_test and not request.user.is_staff:
            qs = TestQuestion.objects.all()[:10]

            context = {
                'questions': qs
            }
        else:
            context = {}
        return render(request, 'personality/aptitude_test.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.applicant.taken_apt_test and not request.user.is_staff:
            choices = [request.POST.get(str(q+1)) for q in range(10)]
            score = 0
            user_choices = TestChoice.objects.filter(pk__in=choices)
            correct_answers = TestChoice.objects.filter(is_answer=True)
            correct_ids = [x.id for x in correct_answers]
            for uc in user_choices:
                if(uc.id in correct_ids):
                    score += 10
            print(score)
            user = User.objects.get(username=request.user.username)
            user.applicant.test_score = score
            user.applicant.taken_apt_test = True
            #user.applicant.is_employable="NULL"
            user.applicant.save()
            return redirect('aptitude_finished')
        else:
            return render(request, 'personality/aptitude_test.html', {})

fscores = []
class PersonalityTest(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.applicant.taken_personality_test and not request.user.is_staff:
            qs = PersonalityType.objects.all()
            type_o = PersonalityType.objects.get(id=1)
            type_c = PersonalityType.objects.get(id=2)
            type_e = PersonalityType.objects.get(id=3)
            type_a = PersonalityType.objects.get(id=4)
            type_n = PersonalityType.objects.get(id=5)

            context = {
                'type_o': type_o,
                'type_c': type_c,
                'type_e': type_e,
                'type_a': type_a,
                'type_n': type_n,
            }
        else:
            context = {}
        return render(request, 'personality/personality_test.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.applicant.taken_personality_test and not request.user.is_staff:
            request_count = len(request.POST)-2
            choices = [int(request.POST.get('choice'+str(q+1))) for q in range(request_count)]
            print(choices)
            average = sum(choices)/len(choices) if len(choices) > 0 else 0

            print(average)
            type_o = PersonalityType.objects.get(id=1)
            type_c = PersonalityType.objects.get(id=2)
            type_e = PersonalityType.objects.get(id=3)
            type_a = PersonalityType.objects.get(id=4)
            type_n = PersonalityType.objects.get(id=5)
            user = User.objects.get(username=request.user.username)

            test_type = request.POST.get('test_type')

            if test_type == '1':
                print('Openness Test')
                request.session['avg_o'] = sum(choices)/len(choices)
                f5 = 8 + choices[0]-choices[1]+choices[2]-choices[3]+choices[4]-choices[5]+choices[6]+choices[7]+choices[8]+choices[9]
                if(f5<20):
                    f5str = 'I'
                else:
                    f5str = 'N'
                print("F5 : ")
                print(f5)
                print(f5str)
                fscores.append(f5str)
                answers = pd.DataFrame([choices])

                request.session['done_o'] = True
            elif test_type == '2':
                print('Consientious Test')
                request.session['avg_c'] = sum(choices)/len(choices)
                f3 = 14 + choices[0]-choices[1]+choices[2]-choices[3]+choices[4]-choices[5]+choices[6]-choices[7]+choices[8]+choices[9]

                if(f3<20):
                    f3str = 'O'
                else:
                    f3str = 'U'
                print("F3 : ")
                print(f3)
                print(f3str)
                fscores.append(f3str)    #pickle_in = open(os.path.join(classifer_base, 'conscientious.pkl'), 'rb')
                answers = pd.DataFrame([choices])
                request.session['done_c'] = True
            elif test_type == '3':
                print('Extroversion Test')
                request.session['avg_e'] = sum(choices)/len(choices)
                f1 = 20 + choices[0]-choices[1]+choices[2]-choices[3]+choices[4]-choices[5]+choices[6]-choices[7]+choices[8]-choices[9]

                if(f1<20):
                    f1str = 'S'
                else:
                    f1str = 'R'
                print("F1 : ")
                print(f1)
                print(f1str)
                fscores.append(f1str)
                answers = pd.DataFrame([choices])
                request.session['done_e'] = True
            elif test_type == '4':
                print('Agreeable Test')
                request.session['avg_a'] = sum(choices)/len(choices)
                f4 = sum(choices)
                f4 = 14 - choices[0]+choices[1]-choices[2]+choices[3]-choices[4]+choices[5]-choices[6]+choices[7]+choices[8]+choices[9]

                if(f4<20):
                    f4str = 'A'
                else:
                    f4str = 'E'
                print("F4 : ")
                print(f4)
                print(f4str)
                fscores.append(f4str)
                answers = pd.DataFrame([choices])

                #result = clf_agb.predict(answers)
                #user.applicant.personality.add(type_a) if result == ['YES'] else None
                request.session['done_a'] = True
            elif test_type == '5':
                print('Neurotism Test')
                request.session['avg_n'] = sum(choices)/len(choices)
                f2 = 38 - choices[0]+choices[1]-choices[2]+choices[3]-choices[4]-choices[5]-choices[6]-choices[7]-choices[8]-choices[9]

                if(f2<20):
                    f2str = 'C'
                else:
                    f2str = 'L'
                print("F2 : ")
                print(f2)
                print(f2str)
                fscores.append(f2str)
                answers = pd.DataFrame([choices])

                request.session['done_n'] = True

                user.applicant.taken_personality_test = True
                user.applicant.save()

                return redirect('personality_completed')


        return redirect('personality_test')


class PersonalityCompleted(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.applicant.taken_personality_test and not request.user.is_staff:
            pickle_in = open(os.path.join(classifer_base, 'employability.pkl'), 'rb')
            clf_emp = pickle.load(pickle_in)
            avg_o = request.session.get('avg_o', None)
            avg_c = request.session.get('avg_c', None)
            avg_e = request.session.get('avg_e', None)
            avg_a = request.session.get('avg_a', None)
            avg_n = request.session.get('avg_n', None)
            averages = [avg_o, avg_c, avg_e, avg_a, avg_n]
            print(averages)
            if len(averages) != 5 or None in averages:
                completed = False
            else:
                personality_avgs = pd.DataFrame([averages])
                #result = clf_emp.predict(personality_avgs)
                #print('Employable', result)
                possible_results = [1,0]
                #if result in possible_results:
                completed = True
                clear_test_session(request)
                user = User.objects.get(username=request.user.username)
                f1str = fscores[2]
                f2str = fscores[4]
                f3str = fscores[1]
                f4str = fscores[3]
                f5str = fscores[0]
                str = f1str+f2str+f3str+f4str+f5str
                print(str)
                user.applicant.is_employable = str
                user.applicant.save()
        else:
            completed = False
        context = {
            'completed': completed
        }
        return render(request, 'personality/personality_completed.html', context)
