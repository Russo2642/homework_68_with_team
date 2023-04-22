from django.shortcuts import render, redirect
from django.views import View
from vacancy.models import Message


class ChatView(View):
    def get(self, request, vacancy_id, applicant_id):
        chat_messages = Message.objects.filter(
            vacancy_id=vacancy_id,
            applicant_id=applicant_id,
        ).order_by('timestamp')

        context = {
            'vacancy_id': vacancy_id,
            'applicant_id': applicant_id,
            'chat_messages': chat_messages,
        }
        return render(request, 'chat.html', context=context)

    def post(self, request, vacancy_id, applicant_id):
        text = request.POST.get('text')
        if text:
            message = Message(
                sender=request.user,
                recipient_id=applicant_id,
                vacancy_id=vacancy_id,
                applicant_id=applicant_id,
                text=text,
            )
            message.save()
        return redirect('chat', vacancy_id=vacancy_id, applicant_id=applicant_id)


class ChatListView(View):
    def get(self, request):
        chats = Message.objects.filter(sender=request.user) | Message.objects.filter(recipient=request.user)
        chats = chats.distinct('vacancy_id', 'applicant_id').order_by('vacancy_id', 'applicant_id')

        context = {
            'chats': chats,
        }
        return render(request, 'chat_list.html', context=context)
