from django.shortcuts import render, HttpResponseRedirect


def get_default_contex():
    """Funkcja zwracająca podstawowy kontekst. """
    return {"sex": ("kobieta", "męzczyzna")}


def view_main_bmi(request):
    """Podstawowy widok kalkulatora bmi."""
    return render(
        request,
        "calculators/bmi.html",
        get_default_contex()
    )


def view_count_bmi(request):
    """Funkcja służąca do obliczeń wartości bmi na podstawie wartości podanych przez użytkownika."""

    # pobranie danych wprowadzonych przez użytkownika
    baza_uczniow = float(request.POST["baza_uczniow"])

    # obliczanie bmi
    zwiekszona_masa_uczniow = round(baza_uczniow * 3)
    ile_ucznia = round(zwiekszona_masa_uczniow * 100 / 70.8)


    # dodanie obliczonych wartości bmi oraz kategori wagowej do słownika request.session
    request.session["zwiekszona_masa_uczniow"] = zwiekszona_masa_uczniow
    request.session["ile_ucznia"] = ile_ucznia

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button !!
    return HttpResponseRedirect("/calculators/bmi_result/")


def view_bmi_result(request):
    """Widok zawierający obliczony wynik bmi dla użytkownika."""
    context = get_default_contex()
    context.update({
        "zwiekszona_masa_uczniow": request.session["zwiekszona_masa_uczniow"],
        "ile_ucznia": request.session["ile_ucznia"]
    })

    return render(
        request,
        "calculators/bmi_results.html",
        context
    )
