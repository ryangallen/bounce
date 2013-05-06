import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import utc
from django.utils.log import getLogger
from django.contrib.auth.decorators import login_required
from stories.models import Story
from stories.forms import StoryForm

logger = getLogger('app')

def score(story, gravity = 1.8, timebase = 120):
	points = (story.points - 1) ** 0.8
	now = datetime.datetime.utcnow().replace(tzinfo = utc)
	age = int((now - story.created_at).total_seconds())/60
	return points/(age + timebase) ** 1.8

def top_stories(top = 200, consider = 1000):
	latest_stories = Story.objects.all().order_by('-created_at')[:consider]
	ranked_stories = sorted([(score(story), story) for story in latest_stories], reverse = True)
	return [story for _, story in ranked_stories][:top]

def index(request):
	stories = top_stories(top = 25)
	if request.user.is_authenticated():
		liked_stories = request.user.liked_stories.filter(id__in = [story.id for story in stories])
	else:
		liked_stories = []
	return render(request, 'stories/index.html', {
		'stories': stories,
		'user': request.user,
		'liked_stories': liked_stories
	})

@login_required
def story(request):
	if request.method == 'POST':
		form = StoryForm(request.POST)
		if form.is_valid():
			story = form.save(commit = False)
			user = request.user
			story.moderator = user
			story.save()
			user.liked_stories.add(story)
			return HttpResponseRedirect('/')
	else:
		form = StoryForm()
	return render(request, 'stories/story.html', {'form': form})

@login_required
def vote(request):
	story = get_object_or_404(Story, pk = request.POST.get('story'))
	user = request.user
	if story not in user.liked_stories.all():
		story.points += 1
		story.save()
		user.liked_stories.add(story)
		user.save()
		logger.info(str(user) + ' voted up "' + str(story.title) + '"')
	return HttpResponse()