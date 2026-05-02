from django.shortcuts import render
from .models import SocialLink, Slider, MovieTheater, Advertisement, Celebrity, Trailer, TrailerItem, Tweet, News, NewsletterSubscriber

def home(request):
<<<<<<< HEAD

    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)

    social_links = SocialLink.objects.all()
    sliders = Slider.objects.all()
    movies_theater = MovieTheater.objects.all()
    ads = Advertisement.objects.all()
    celebrities = Celebrity.objects.all()
    trailers = Trailer.objects.all()
    trailer_items = TrailerItem.objects.all()
    tweets = Tweet.objects.all()
    news_main = News.objects.filter(section="main").first()
    news_side = News.objects.filter(section="side")

    return render(request, 'index.html', {
        'social_links': social_links,
        'sliders': sliders,
        'movies_theater': movies_theater,
        'ads': ads,
        'celebrities': celebrities,
        'trailers': trailers,
        'trailer_items': trailer_items,
        'tweets': tweets,
        'news_main': news_main,
        'news_side': news_side,
    })
=======
    return render(request, 'mainapp/index.html')
>>>>>>> 3988b77cc86ec854ecce1b13ab0183ad8bba35a9
