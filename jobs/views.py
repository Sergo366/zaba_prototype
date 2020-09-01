import redis
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from adverts.utils import context_helper
from .filters import JobsFilter
from .models import Job
from .form import JobForm

# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)


def index(request):
    query = request.GET.get('q')
    lang = request.LANGUAGE_CODE
    if query:
        advert_list = Job.objects.filter(Q(local__exact=lang)
                                            & (Q(title__icontains=query) | Q(description__icontains=query))
                                            ).order_by('-modified')
    else:
        advert_list = Job.objects.filter(local=lang).order_by('-modified')

    filters = JobsFilter(request.GET, queryset=advert_list)
    adverts, has_filter = context_helper(request, filters)

    context = {'adverts': adverts,
               'filters': filters,
               'has_filter': has_filter,
               'package_list': 'jobs:index',
               }

    return render(request, 'jobs/index.html', context)


def detail(request, advert_id):
    advert = get_object_or_404(Job, pk=advert_id)
    total_views = r.incr('job:{}:views'.format(advert.id))
    return render(request, 'jobs/detail.html', {'advert': advert, 'total_views': total_views})


class JobList(ListView):
    queryset = Job.objects.filter(point__isnull=False)


class JobCreate(CreateView):
    model = Job
    form_class = JobForm
    login_required = True
    success_url = reverse_lazy('jobs:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class JobUpdate(UpdateView):
    model = Job
    login_required = True
    form_class = JobForm
    success_url = reverse_lazy('jobs:index')


class JobDelete(DeleteView):
    model = Job
    login_required = True
    success_url = reverse_lazy('jobs:index')
