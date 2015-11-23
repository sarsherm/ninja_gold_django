from django.shortcuts import render, redirect
import random
from datetime import datetime
time = datetime.now()

def index(request):
	try:
		request.session["gold"]
	except:
		request.session["gold"] = 0
	try:
		request.session["message"]
	except:
		request.session["message"] = []
	return render(request, 'golds/index.html')

def process_money(request):
	if request.POST['action'] == 'farm':
		gold = random.randrange(10, 21)
		request.session["gold"] += gold
		note = "Earned %d golds from the farm! %s" %(gold, time)
		request.session["message"].append(note)
	elif request.POST['action'] == 'cave':
		gold = random.randrange(5, 11)
		request.session["gold"] += gold
		note = "Earned %d golds from the cave! %s" %(gold, time)
		request.session["message"].append(note)
	elif request.POST['action'] == 'house':
		gold = random.randrange(2, 6)
		request.session["gold"] += gold
		note = "Earned %d golds from the cave! %s" %(gold, time)
		request.session["message"].append(note)
	elif request.POST['action'] == 'casino':
		luck = random.randrange(1, 11)
		gold = random.randrange(5, 11)
		if luck >= 5:
			request.session["gold"]-= gold
			note = "Lost %d golds from the casino! %s" %(gold, time)
			request.session["message"].append(note)
		else:
			request.session["gold"] += gold
			note = "Earned %d golds from the cave! %s" %(gold, time)
			request.session["message"].append(note)
	return redirect('/')
