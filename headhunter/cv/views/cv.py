import io

from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from cv.forms import CVForm
from cv.forms import JobExpForm
from cv.models.cv import CV
from cv.models import JobExperience
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from vacancy.models import Application


class CVCreateView(CreateView):
    template_name = 'cv/cv_create.html'
    model = CV
    form_class = CVForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job_create', kwargs={'pk': self.object.pk})


class CVDetailView(DetailView):
    template_name = 'cv/cv_detail.html'
    model = CV
    context_object_name = 'cv'


class CVUpdateView(UpdateView):
    template_name = 'cv/cv_update.html'
    model = CV
    form_class = CVForm

    def get_success_url(self):
        return reverse('cv_detail', kwargs={'pk': self.object.pk})


class CVDeleteView(UserPassesTestMixin, DeleteView):
    model = CV

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user_id})

    def test_func(self):
        return self.get_object().user == self.request.user


class JobExpCreateView(CreateView):
    template_name = 'cv/job_create.html'
    model = JobExperience
    form_class = JobExpForm

    def form_valid(self, form):
        cv = get_object_or_404(CV, pk=self.kwargs.get('pk'))
        job_exp = form.save(commit=False)
        job_exp.cv = cv
        job_exp.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class JobExpUpdateView(UpdateView):
    template_name = 'cv/job_update.html'
    model = JobExperience
    form_class = JobExpForm
    context_object_name = 'job_exp'

    def get_success_url(self):
        return reverse('cv_detail', kwargs={'pk': self.object.cv_id})


class UpdateButtonView(View):
    def post(self, request, pk):
        cv = get_object_or_404(CV, pk=pk)
        cv.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class IsPublishedView(View):
    def post(self, request, pk):
        cv = get_object_or_404(CV, pk=pk)
        if cv.is_published:
            cv.is_published = False
        else:
            cv.is_published = True
        cv.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class CVListView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_employer:
            applications = Application.objects.filter(vacancy__author=request.user)
            applicant_ids = [app.applicant.id for app in applications]
            cvs = CV.objects.filter(user__id__in=applicant_ids)
        else:
            cvs = CV.objects.filter(user=request.user)

        context = {
            'cvs': cvs,
        }
        return render(request, 'cv/cv_list.html', context=context)


def get_to_pdf(request, pk):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)
    cvs = CV.objects.filter(pk=pk)
    lines = []
    for cv in cvs:
        lines.append(f"{request.user.first_name} {request.user.last_name}")
        lines.append(cv.title)
        lines.append(f"Category - {cv.category}")
        lines.append(f"Email - {cv.email}")
        lines.append(f"Phone - {cv.phone}")
        lines.append(f"Salary - {cv.salary}")
        lines.append(f"Date of birth - {cv.date_birth}")
        lines.append(f"Sex - {cv.sex}")
        lines.append(f"Marital status - {cv.marital_status}")
        lines.append(f"Address 1 - {cv.address1}")
        lines.append(f"Address 2 - {cv.address2}")
        lines.append(f"City - {cv.city}")
        lines.append(f"Telegram - {cv.telegram}")
        lines.append(f"Whatsapp - {cv.whatsapp}")
        lines.append(f"Linkedin - {cv.linkedin}")
        lines.append(f"Facebook - {cv.facebook}")
        lines.append(f"CV created at - {cv.created_at}")
        lines.append(" ")
        lines.append("Job experience")
        for job in cv.job_exp.all():
            lines.append(f"Company - {job.job_place}")
            lines.append(f"Standing - {job.job_exp}")
            lines.append(f"Position - {job.job_position}")
            lines.append(f"Description - {job.job_description}")
    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(
        buffer,
        as_attachment=True,
        filename=f"CV_{request.user.first_name}_{request.user.last_name}.pdf"
    )
