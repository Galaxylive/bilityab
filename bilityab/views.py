# -*- coding: utf-8 -*-
from django.db.models import Sum
from django.shortcuts import render
from event.models import Event, Categories, Showtime, PositionPrice


def get_type(event_id):
    sub_category = Categories.objects.get(id=Event.objects.get(id=event_id).category_id)
    category = Categories.objects.get(id=sub_category.parent_id).title
    return {
        'ورزشی': 'sport',
        'سینمایی': 'cinema',
        'موسیقی': 'music',
        'گردشگری': 'tourism'
    }[category]


def make_event_type_list(event_list):
    event_type_list = []
    for event in event_list:
        category = get_type(event.id)
        event_type_list.append((event, category))

    return event_type_list


def make_event_type_list1(event_list):
    event_type_list = []
    for event in event_list:
        category = get_type(event.id)
        organizer = event.event_organizers.all()[0]
        dates = Showtime.objects.filter(event=event)
        print(organizer, event)
        position_price = PositionPrice.objects.get(organizer=organizer, event=event)
        total_capacity = 0
        for show_time in event.show_times.all():
            total_capacity += show_time.capacity
        if dates:
            date = get_nearest_date(dates)
            event_type_list.append((event, category, organizer, date, total_capacity, position_price.price))
        else:
            event_type_list.append((event, category, organizer, total_capacity, position_price.price))
    return event_type_list


def get_nearest_date(dates):
    if dates:
        result = dates[0]
        for date in dates:
            if date.date < result.date:
                result = date
        return result


def home(request):

    return render(request, 'home.html', {
        'bestEvents': make_event_type_list1(Event.objects.annotate(rate=Sum('rates')).order_by('-rates')[:3]),
        # 'nearestEvents': make_event_type_list1(Event.objects.all().order_by('-show_times__date')[:3]),
        'newestEvents': make_event_type_list1(Event.objects.all().order_by('-created_at')[:3]),
        'actionMovies': make_event_type_list1(Event.objects.filter(category__title='اکشن')),
        'dramaticMovies': make_event_type_list1(Event.objects.filter(category__title='درام')),
        'comicMovies': make_event_type_list1(Event.objects.filter(category__title='کمدی')),
        'volleyballEvents': make_event_type_list1(Event.objects.filter(category__title='والیبال')),
        'footballEvents': make_event_type_list1(Event.objects.filter(category__title='فوتبال')),
        'basketballEvents': make_event_type_list1(Event.objects.filter(category__title='بسکتبال')),
        'wrestleEvents': make_event_type_list1(Event.objects.filter(category__title='کشتی')),
        'zooEvents': make_event_type_list1(Event.objects.filter(category__title='باغ وحش')),
        'amusementEvents': make_event_type_list1(Event.objects.filter(category__title='شهر بازی')),
        'circusEvents': make_event_type_list1(Event.objects.filter(category__title='سیرک')),
        'traditionalMusic': make_event_type_list1(Event.objects.filter(category__title='سنتی')),
        'popMusic': make_event_type_list1(Event.objects.filter(category__title='پاپ')),
        'suggestedEvents': make_event_type_list1(Event.objects.all()[:3]),
        'logged_in': request.user.is_authenticated()

    })


def terms(request):
    return render(request, 'terms.html', {
        'pageTitle': " - شرایط و ضوابط",
        'logged_in': request.user.is_authenticated()

    })


def about(request):
    return render(request, 'about.html', {
        'pageTitle': " - درباره",
        'logged_in': request.user.is_authenticated()

    })


def contact(request):
    return render(request, 'contact-us.html', {
        'pageTitle': " - تماس با ما",
        'logged_in': request.user.is_authenticated()

    })
