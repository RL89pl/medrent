from django.core.management.base import BaseCommand
from core.models import Category, Product


CATEGORIES = [
    {'name': 'Wózki Inwalidzkie',              'slug': 'wozki-inwalidzkie',       'icon_key': 'wheelchair',   'order': 1},
    {'name': 'Sprzęt Łazienkowy',              'slug': 'sprzet-lazienkowy',        'icon_key': 'bath',         'order': 2},
    {'name': 'Łóżka Rehabilitacyjne',          'slug': 'lozka-rehabilitacyjne',    'icon_key': 'bed',          'order': 3},
    {'name': 'Materace Przeciwodleżynowe',     'slug': 'materace',                 'icon_key': 'mattress',     'order': 4},
    {'name': 'Sprzęt do Chodzenia',            'slug': 'sprzet-do-chodzenia',      'icon_key': 'walking',      'order': 5},
    {'name': 'Sprzęt Toaletowy i Higiena',     'slug': 'sprzet-toaletowy',         'icon_key': 'toilet',       'order': 6},
    {'name': 'Fotele Geriatryczne',            'slug': 'fotele-geriatryczne',      'icon_key': 'chair',        'order': 7},
    {'name': 'Tlenoterapia i Elektromedycyna', 'slug': 'tlenoterapia',             'icon_key': 'oxygen',       'order': 8},
    {'name': 'Ortopedia i Stabilizatory',      'slug': 'ortopedia',                'icon_key': 'ortho',        'order': 9},
]

PRODUCTS = [
    # ── WÓZKI ELEKTRYCZNE ────────────────────────────────────────────────────
    {
        'category': 'wozki-inwalidzkie',
        'subcategory': 'Wózki Elektryczne',
        'name': 'iFold',
        'badge': '5 lat gwarancji',
        'max_load': '150 kg',
        'warranty_years': 5,
        'short_description': 'Składany wózek elektryczny z automatycznym składaniem i odchylanym oparciem.',
        'long_description': (
            'iFold to nowoczesny wózek elektryczny zaprojektowany z myślą o komforcie i mobilności. '
            'Automatyczne składanie umożliwia szybkie przygotowanie wózka do transportu. '
            'Elektryczny i manualny tryb jazdy daje elastyczność użytkowania.'
        ),
        'specs': [
            {'label': 'Zasięg', 'value': '≤ 20 km'},
            {'label': 'Prędkość maksymalna', 'value': '6 km/h'},
            {'label': 'Maks. obciążenie', 'value': '150 kg'},
            {'label': 'Szerokość całkowita', 'value': '65 cm'},
            {'label': 'Wysokość całkowita', 'value': '125 cm'},
            {'label': 'Głębokość siedziska', 'value': '47 cm'},
            {'label': 'Wys. siedziska od podłoża', 'value': '53 cm'},
            {'label': 'Waga', 'value': '31,5 kg'},
            {'label': 'Szerokość po złożeniu', 'value': '64 cm'},
            {'label': 'Dostępna szerokość siedziska', 'value': '47 cm'},
        ],
        'features': [
            'Elektryczny i manualny tryb jazdy',
            'Automatyczne składanie i odchylane oparcie',
            'Hamulce elektromagnetyczne',
            'Zagłówek w zestawie',
            'Tylne koła pompowane',
            'Certyfikat CE – wyrób medyczny',
        ],
    },
    {
        'category': 'wozki-inwalidzkie',
        'subcategory': 'Wózki Elektryczne',
        'name': 'POWER-TIM',
        'badge': '5 lat gwarancji',
        'max_load': '130 kg',
        'warranty_years': 5,
        'short_description': 'Wydajny wózek elektryczny z silnikami bezszczotkowymi i dodatkowym joystickiem.',
        'long_description': (
            'POWER-TIM wyróżnia się silnikami bezszczotkowymi, które zapewniają dłuższy czas eksploatacji '
            'i cichą pracę. Dodatkowy joystick dla opiekuna umożliwia asystowanie przy prowadzeniu wózka.'
        ),
        'specs': [
            {'label': 'Zasięg', 'value': '20–25 km'},
            {'label': 'Prędkość maksymalna', 'value': '6 km/h'},
            {'label': 'Maks. obciążenie', 'value': '130 kg'},
            {'label': 'Szerokość całkowita', 'value': '69 cm'},
            {'label': 'Wysokość całkowita', 'value': '91 cm'},
            {'label': 'Głębokość siedziska', 'value': '42,5 cm'},
            {'label': 'Wys. siedziska od podłoża', 'value': '52 cm'},
            {'label': 'Waga', 'value': '28 kg'},
            {'label': 'Szerokość po złożeniu', 'value': '44 cm'},
            {'label': 'Dostępna szerokość siedziska', 'value': '49 cm'},
        ],
        'features': [
            'Silniki bezszczotkowe',
            'Elektryczny i manualny tryb jazdy',
            'Hamulce elektromagnetyczne',
            'Joystick dodatkowy dla opiekuna',
            'Tylne koła pompowane',
            'Certyfikat CE – wyrób medyczny',
        ],
    },
    {
        'category': 'wozki-inwalidzkie',
        'subcategory': 'Wózki Elektryczne',
        'name': 'FortiGO',
        'badge': '5 lat gwarancji',
        'max_load': '150 kg',
        'warranty_years': 5,
        'short_description': 'Wózek elektryczny z regulacją wysokości oparcia i zasięgiem do 20 km.',
        'long_description': (
            'FortiGO łączy wytrzymałość z ergonomią. Regulacja wysokości oparcia zapewnia komfort '
            'dopasowany do użytkownika, a elektryczny i manualny tryb jazdy gwarantuje elastyczność.'
        ),
        'specs': [
            {'label': 'Zasięg', 'value': '≤ 20 km'},
            {'label': 'Prędkość maksymalna', 'value': '6 km/h'},
            {'label': 'Maks. obciążenie', 'value': '150 kg'},
        ],
        'features': [
            'Elektryczny i manualny tryb jazdy',
            'Regulacja wysokości oparcia',
            'Hamulce elektromagnetyczne',
            'Certyfikat CE – wyrób medyczny',
        ],
    },
    {
        'category': 'wozki-inwalidzkie',
        'subcategory': 'Wózki Elektryczne',
        'name': 'ELECTRIC-TIM I',
        'badge': '5 lat gwarancji',
        'max_load': '120 kg',
        'warranty_years': 5,
        'short_description': 'Elektryczny wózek inwalidzki z dużymi kołami i silnikami bezszczotkowymi.',
        'long_description': (
            'ELECTRIC-TIM I oferuje doskonałą manewrowość dzięki dużym kołom tylnym. '
            'Silniki bezszczotkowe w połączeniu z hamulcami elektromagnetycznymi zapewniają bezpieczną jazdę.'
        ),
        'specs': [
            {'label': 'Zasięg', 'value': '≤ 20 km'},
            {'label': 'Prędkość maksymalna', 'value': '6 km/h'},
            {'label': 'Maks. obciążenie', 'value': '120 kg'},
        ],
        'features': [
            'Silniki bezszczotkowe',
            'Hamulce elektromagnetyczne',
            'Duże koła – możliwość sterowania',
            'Elektryczny i manualny tryb jazdy',
            'Certyfikat CE – wyrób medyczny',
        ],
    },
    # ── WÓZKI MANUALNE ───────────────────────────────────────────────────────
    {
        'category': 'wozki-inwalidzkie',
        'subcategory': 'Wózki Aluminiowe',
        'name': 'Wózek Inwalidzki Aluminiowy',
        'max_load': '120 kg',
        'short_description': 'Lekki wózek aluminiowy – składany, z regulowanymi podnóżkami.',
        'long_description': (
            'Klasyczny wózek aluminiowy dostępny w kilku szerokościach siedziska. '
            'Lekka konstrukcja ułatwia codzienne użytkowanie i transport.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '120 kg'},
            {'label': 'Materiał ramy', 'value': 'Aluminium'},
        ],
        'features': ['Składany', 'Regulowane podnóżki', 'Zdejmowane podłokietniki', 'Certyfikat CE'],
    },
    {
        'category': 'wozki-inwalidzkie',
        'subcategory': 'Wózki Aluminiowe',
        'name': 'Wózek Aluminiowy Lekki (do 12 kg)',
        'max_load': '100 kg',
        'short_description': 'Ultra-lekki wózek do 12 kg – idealny w podróży i do aktywnych użytkowników.',
        'long_description': (
            'Waga poniżej 12 kg sprawia, że wózek jest wyjątkowo łatwy w transporcie – '
            'wsiadanie do samochodu, autobusu czy samolotu nie stanowi problemu.'
        ),
        'specs': [
            {'label': 'Waga wózka', 'value': '< 12 kg'},
            {'label': 'Maks. obciążenie', 'value': '100 kg'},
        ],
        'features': ['Ultra-lekki', 'Składany', 'Łatwy transport', 'Certyfikat CE'],
    },
    {
        'category': 'wozki-inwalidzkie',
        'subcategory': 'Wózki Bariatryczne',
        'name': 'BIG-TIM – Wózek Stalowy Bariatryczny',
        'max_load': '225 kg',
        'short_description': 'Wzmocniony wózek stalowy XXL dla pacjentów bariatrycznych.',
        'long_description': (
            'BIG-TIM to wózek wykonany z wzmocnionej stali, przystosowany do znacznie większego '
            'obciążenia. Dostępny również w wersji z funkcją toaletową (COMPLEX-TIM).'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '225 kg'},
            {'label': 'Materiał ramy', 'value': 'Stal wzmocniona'},
        ],
        'features': ['Bariatryczny XXL', 'Wzmocniona rama stalowa', 'Szerokie siedzisko', 'Certyfikat CE'],
    },
    # ── SPRZĘT ŁAZIENKOWY ────────────────────────────────────────────────────
    {
        'category': 'sprzet-lazienkowy',
        'name': 'Taboret Prysznicowy Okrągły',
        'max_load': '136 kg',
        'short_description': 'Aluminiowy taboret prysznicowy z regulowanymi nóżkami – montaż bez narzędzi.',
        'long_description': (
            'Taboret TGR-R KP-O 3432 wykonany z aluminium z antypoślizgowymi nakładkami na nóżkach. '
            'System TF umożliwia montaż bez użycia narzędzi.'
        ),
        'specs': [
            {'label': 'Wysokość całkowita', 'value': '36–54 cm'},
            {'label': 'Średnica siedziska', 'value': '32 cm'},
            {'label': 'Maks. obciążenie', 'value': '136 kg'},
        ],
        'features': ['Regulowane nóżki', 'System TF – montaż bez narzędzi', 'Antypoślizgowe stopki', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-lazienkowy',
        'name': 'Krzesło Prysznicowe',
        'max_load': '136 kg',
        'short_description': 'Krzesło prysznicowe z oparciem, regulowanymi nóżkami i miękkimi uchwytami.',
        'long_description': (
            'Model TGR-R KP 355L wyposażony w miękkie piankowe uchwyty boczne i oparcie dla pleców. '
            'Regulowana wysokość siedzeń i system TF montażu bez narzędzi.'
        ),
        'specs': [
            {'label': 'Szerokość całkowita', 'value': '48 cm'},
            {'label': 'Wysokość całkowita', 'value': '66–79 cm'},
            {'label': 'Głębokość całkowita', 'value': '40 cm'},
            {'label': 'Wys. siedziska od podłoża', 'value': '37–49 cm'},
            {'label': 'Wymiary siedziska', 'value': '40 × 33 cm'},
            {'label': 'Maks. obciążenie', 'value': '136 kg'},
        ],
        'features': ['Oparcie dla pleców', 'Miękkie piankowe uchwyty', 'Regulowane nóżki', 'System TF – montaż bez narzędzi', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-lazienkowy',
        'name': 'Taboret Prysznicowy z Obrotowym Siedziskiem',
        'max_load': '110 kg',
        'short_description': 'Taboret prysznicowy z obrotowym siedziskiem ułatwiającym transfer.',
        'long_description': (
            'Model TGR-R KP-O 5021 z siedziskiem obrotowym o 360° – ułatwia wchodzenie i wychodzenie '
            'spod prysznica. Regulowane nóżki i system TF.'
        ),
        'specs': [
            {'label': 'Wysokość całkowita', 'value': '34,5–52 cm'},
            {'label': 'Średnica siedziska', 'value': '32 cm'},
            {'label': 'Maks. obciążenie', 'value': '110 kg'},
        ],
        'features': ['Obrotowe siedzisko 360°', 'Regulowane nóżki', 'System TF', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-lazienkowy',
        'name': 'Taboret Prysznicowy Przyścienny',
        'max_load': '136 kg',
        'short_description': 'Składany taboret montowany do ściany – odporny na wilgoć.',
        'long_description': (
            'Model JMC-C 5105 mocowany do ściany – po złożeniu nie zajmuje miejsca. '
            'Konstrukcja odporna na wilgoć, idealna do łazienek rehabilitacyjnych.'
        ),
        'specs': [
            {'label': 'Szerokość całkowita', 'value': '40 cm'},
            {'label': 'Wys. siedziska od podłoża', 'value': '42–52 cm'},
            {'label': 'Wymiary siedziska', 'value': '32 × 40 cm'},
            {'label': 'Maks. obciążenie', 'value': '136 kg'},
        ],
        'features': ['Mocowany do ściany', 'Składana konstrukcja', 'Odporny na wilgoć', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-lazienkowy',
        'name': 'Ławka do Wanny z Oparciem (BathTim)',
        'max_load': '136 kg',
        'short_description': 'Ławka umieszczana w wannie z oparciem – ułatwia kąpiel osobom mniej sprawnym.',
        'long_description': (
            'BathTim to ławka do wanny z oparciem i regulowanymi nóżkami. '
            'Dwie nogi znajdują się w wannie, dwie na zewnątrz – co umożliwia bezpieczne przesiadanie.'
        ),
        'specs': [{'label': 'Maks. obciążenie', 'value': '136 kg'}],
        'features': ['Oparcie w zestawie', 'Regulowana wysokość', 'Antypoślizgowe stopki', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-lazienkowy',
        'name': 'Uchwyt Łazienkowy Prosty HOLD-TIM',
        'max_load': '150 kg',
        'short_description': 'Ścienny uchwyt łazienkowy ze stali nierdzewnej – wyrób medyczny.',
        'long_description': (
            'HOLD-TIM to solidny uchwyt montowany do ściany, wykonany ze stali nierdzewnej. '
            'Dostępny w różnych długościach i kątach montażu.'
        ),
        'specs': [{'label': 'Maks. obciążenie', 'value': '150 kg'}],
        'features': ['Stal nierdzewna', 'Montaż ścienny', 'Wyrób medyczny CE', 'Różne długości'],
    },
    # ── ŁÓŻKA ────────────────────────────────────────────────────────────────
    {
        'category': 'lozka-rehabilitacyjne',
        'name': 'DREAM-TIM – Łóżko Elektryczne',
        'badge': 'Nowość',
        'max_load': '150 kg',
        'warranty_years': 2,
        'short_description': 'Elektryczne łóżko rehabilitacyjne z regulacją pleców, nóg i wysokości.',
        'long_description': (
            'DREAM-TIM to elektryczne łóżko rehabilitacyjne wyposażone w trzy segmenty regulacji: '
            'plecy, nogi i wysokość łóżka. Pilot w zestawie, barierki ochronne w opcji. '
            'Dostępne w wykończeniu Dąb Sonoma i Buk.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '150 kg'},
            {'label': 'Segmenty regulacji', 'value': '3 (plecy, nogi, wysokość)'},
            {'label': 'Napęd', 'value': 'Elektryczny'},
            {'label': 'Wykończenie', 'value': 'Dąb Sonoma / Buk'},
        ],
        'features': ['Regulacja elektryczna 3 segmenty', 'Pilot w zestawie', 'Barierki ochronne', 'Certyfikat CE – wyrób medyczny'],
    },
    {
        'category': 'lozka-rehabilitacyjne',
        'name': 'DREAM-TIM LOW – Łóżko Niskie Elektryczne',
        'max_load': '150 kg',
        'warranty_years': 2,
        'short_description': 'Wersja niska łóżka elektrycznego – minimalizuje ryzyko upadku.',
        'long_description': (
            'DREAM-TIM LOW to wersja o obniżonej pozycji spoczynkowej, dedykowana pacjentom '
            'z podwyższonym ryzykiem upadku z łóżka. Zachowuje pełną funkcjonalność elektrycznej regulacji.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '150 kg'},
            {'label': 'Min. wysokość leżenia', 'value': 'Obniżona'},
            {'label': 'Napęd', 'value': 'Elektryczny'},
        ],
        'features': ['Obniżona pozycja spoczynkowa', 'Regulacja elektryczna', 'Pilot w zestawie', 'Certyfikat CE'],
    },
    {
        'category': 'lozka-rehabilitacyjne',
        'name': 'DREAM-TIM MAX – Łóżko Bariatryczne',
        'max_load': '230 kg',
        'warranty_years': 2,
        'short_description': 'Elektryczne łóżko bariatryczne dla pacjentów wymagających wzmocnionej konstrukcji.',
        'long_description': (
            'DREAM-TIM MAX to bariatryczna wersja łóżka elektrycznego z wzmocnioną ramą. '
            'Dostępny również w wersji niskiej (DREAM-TIM MAX LOW).'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '230 kg'},
            {'label': 'Napęd', 'value': 'Elektryczny'},
        ],
        'features': ['Bariatryczny XXL', 'Wzmocniona rama', 'Regulacja elektryczna', 'Pilot w zestawie', 'Certyfikat CE'],
    },
    # ── MATERACE ─────────────────────────────────────────────────────────────
    {
        'category': 'materace',
        'name': 'Materac Przeciwodleżynowy Rurowy',
        'max_load': '130 kg',
        'short_description': 'Materac ze zmiennym ciśnieniem i cichobieżnym kompresorem w zestawie.',
        'long_description': (
            'Materac rurowy ze zmiennym ciśnieniem powietrza zmniejsza ryzyko odleżyn. '
            'Cichy kompresor zapewnia naprzemienne pompowanie i opróżnianie komór.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '130 kg'},
            {'label': 'Typ', 'value': 'Zmienna presja – rurowy'},
        ],
        'features': ['Zmienna presja', 'Kompresor w zestawie', 'Cicha praca', 'Certyfikat CE'],
    },
    {
        'category': 'materace',
        'name': 'TurnMATE – Materac z Funkcją Zmiany Pozycji',
        'max_load': '200 kg',
        'short_description': 'Bariatryczny materac z automatyczną zmianą pozycji pacjenta.',
        'long_description': (
            'TurnMATE to zaawansowany materac z funkcją automatycznej zmiany pozycji ciała, '
            'dedykowany pacjentom bariatrycznym i osobom leżącym przez długi czas.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '200 kg'},
            {'label': 'Typ', 'value': 'Bariatryczny z funkcją zmiany pozycji'},
        ],
        'features': ['Automatyczna zmiana pozycji', 'Bariatryczny', 'Redukcja odleżyn', 'Certyfikat CE'],
    },
    {
        'category': 'materace',
        'name': 'Materac Piankowy Przeciwodleżynowy',
        'max_load': '120 kg',
        'short_description': 'Materac z pianki HR z pokrywą odporną na wilgoć i środki dezynfekujące.',
        'long_description': (
            'Wykonany z pianki wysokoelastycznej HR, zapewniającej odpowiednie rozłożenie ciśnienia. '
            'Zmywalna pokrywa odporna na środki dezynfekujące.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '120 kg'},
            {'label': 'Typ', 'value': 'Pianka HR'},
        ],
        'features': ['Pianka wysokoelastyczna HR', 'Zmywalna pokrywa', 'Różne rozmiary', 'Certyfikat CE'],
    },
    # ── SPRZĘT DO CHODZENIA ──────────────────────────────────────────────────
    {
        'category': 'sprzet-do-chodzenia',
        'name': 'Balkonik Rehabilitacyjny',
        'short_description': 'Lekki aluminiowy balkonik składany z regulowaną wysokością.',
        'long_description': (
            'Klasyczny balkonik aluminiowy z możliwością regulacji wysokości uchwytu. '
            'Składana konstrukcja ułatwia przechowywanie i transport.'
        ),
        'specs': [
            {'label': 'Materiał', 'value': 'Aluminium'},
            {'label': 'Regulacja wysokości', 'value': 'Tak'},
        ],
        'features': ['Składany', 'Regulowana wysokość', 'Lekkie aluminium', 'Antypoślizgowe stopki'],
    },
    {
        'category': 'sprzet-do-chodzenia',
        'name': 'Kule Łokciowe (para)',
        'short_description': 'Aluminiowe kule łokciowe – regulowane, ergonomiczne uchwyty.',
        'long_description': (
            'Para kul łokciowych z ergonomicznymi uchwytami i regulowaną długością. '
            'Obejmę łokciową można szybko dopasować do użytkownika.'
        ),
        'specs': [
            {'label': 'Materiał', 'value': 'Aluminium'},
            {'label': 'Regulacja', 'value': 'Tak'},
        ],
        'features': ['Para w zestawie', 'Ergonomiczne uchwyty', 'Regulowane', 'Antypoślizgowe końcówki'],
    },
    {
        'category': 'sprzet-do-chodzenia',
        'name': 'Chodzik na Kółkach z Siedziskiem',
        'short_description': 'Chodzik 4-kołowy z siedziskiem, hamulcami i koszem.',
        'long_description': (
            'Czterokołowy chodzik (rollator) z siedziskiem umożliwiającym odpoczynek podczas marszu. '
            'Wyposażony w hamulce ręczne i kosz pod siedziskiem.'
        ),
        'specs': [
            {'label': 'Kółka', 'value': '4'},
            {'label': 'Siedzisko', 'value': 'Tak'},
        ],
        'features': ['Siedzisko', 'Hamulce ręczne', 'Kosz w zestawie', 'Składany', 'Regulowana wysokość'],
    },
    {
        'category': 'sprzet-do-chodzenia',
        'name': 'Podpórka Czterokołowa YOLA',
        'short_description': 'Elegancka podpórka 4-kołowa z turkusowym wykończeniem – linia YOLA.',
        'long_description': (
            'YOLA to linia podpórek aluminiowych dostępna w kolorze turkusowym. '
            'Wersja YOLA AIR wykonana z aluminium lotniczego jest jeszcze lżejsza.'
        ),
        'specs': [
            {'label': 'Materiał', 'value': 'Aluminium'},
            {'label': 'Kolor', 'value': 'Turkusowy'},
        ],
        'features': ['4 kółka', 'Składana', 'Regulowana wysokość', 'Wersja AIR – ultralight'],
    },
    # ── SPRZĘT TOALETOWY ─────────────────────────────────────────────────────
    {
        'category': 'sprzet-toaletowy',
        'name': 'Krzesło Toaletowe MAXIMUS',
        'max_load': '230 kg',
        'short_description': 'Bariatryczne krzesło toaletowo-prysznicowe 3w1 – składane.',
        'long_description': (
            'MAXIMUS to bariatryczne krzesło łączące funkcje: krzesła toaletowego, prysznicowego '
            'i toaletki. Wzmocniona konstrukcja dla pacjentów do 230 kg.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '230 kg'},
            {'label': 'Funkcje', 'value': '3w1: toaletowe, prysznicowe'},
        ],
        'features': ['Bariatryczne XXL', 'Składane', 'Regulowane nóżki', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-toaletowy',
        'name': 'Wózek Toaletowo-Prysznicowy MASTER-TIM',
        'max_load': '120 kg',
        'short_description': 'Wózek prysznicowo-toaletowy 3w1 umożliwiający transport pod prysznic.',
        'long_description': (
            'MASTER-TIM pozwala na transport pacjenta bezpośrednio pod prysznic bez konieczności '
            'przekładania. Dostępny w wersji MASTER-TIM PLUS z dodatkowymi funkcjami.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '120 kg'},
            {'label': 'Typ', 'value': 'Transport + toaleta + prysznic'},
        ],
        'features': ['Transport pod prysznic', 'Barierki boczne', 'Kółka z blokadą', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-toaletowy',
        'name': 'Nasadka Toaletowa z Uchwytami',
        'max_load': '130 kg',
        'short_description': 'Podwyższona nasadka toaletowa z uchwytami bocznymi.',
        'long_description': (
            'Nasadka zwiększa wysokość toalety, co ułatwia siadanie i wstawanie. '
            'Uchwyty boczne zapewniają dodatkowe podparcie i bezpieczeństwo.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '130 kg'},
            {'label': 'Podwyższenie', 'value': 'ok. 10 cm'},
        ],
        'features': ['Podwyższona', 'Uchwyty boczne', 'Antypoślizgowa', 'Certyfikat CE'],
    },
    {
        'category': 'sprzet-toaletowy',
        'name': 'Podnośnik Transferowy SAFE-TRANSFER',
        'max_load': '200 kg',
        'short_description': 'Hydrauliczny podnośnik transferowy dla pacjentów bariatrycznych.',
        'long_description': (
            'SAFE-TRANSFER to hydrauliczny podnośnik ułatwiający bezpieczny transfer pacjenta '
            'między łóżkiem, fotelem i wózkiem. Idealny dla opiekunów domowych.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '200 kg'},
            {'label': 'Napęd', 'value': 'Hydrauliczny'},
        ],
        'features': ['Hydrauliczny', 'Bariatryczny', 'Bezpieczny transfer', 'Certyfikat CE'],
    },
    # ── FOTELE GERIATRYCZNE ──────────────────────────────────────────────────
    {
        'category': 'fotele-geriatryczne',
        'name': 'Fotel Geriatryczny Pionizujący RELAX',
        'max_load': '120 kg',
        'short_description': 'Elektryczny fotel geriatryczny z funkcją pionizacji i regulowanym oparciem.',
        'long_description': (
            'RELAX to fotel z elektryczną funkcją pionizacji – wstanie staje się znacznie łatwiejsze. '
            'Regulowane oparcie i chowany podnóżek zapewniają pełen komfort odpoczynku.'
        ),
        'specs': [
            {'label': 'Maks. obciążenie', 'value': '120 kg'},
            {'label': 'Napęd pionizacji', 'value': 'Elektryczny'},
        ],
        'features': ['Elektryczna funkcja pionizacji', 'Regulowane oparcie', 'Chowany podnóżek', 'Pilot w zestawie', 'Certyfikat CE'],
    },
    # ── TLENOTERAPIA ─────────────────────────────────────────────────────────
    {
        'category': 'tlenoterapia',
        'subcategory': 'Koncentratory Tlenu',
        'name': 'Koncentrator Tlenu 8F-10',
        'max_load': '',
        'short_description': 'Stacjonarny koncentrator tlenu do 10 l/min z czujnikiem stężenia.',
        'long_description': (
            '8F-10 to stacjonarny koncentrator tlenu wyposażony w czujnik stężenia O₂ '
            'informujący o jakości dostarczanego tlenu. Cicha praca poniżej 48 dB.'
        ),
        'specs': [
            {'label': 'Wydajność', 'value': 'Do 10 l/min'},
            {'label': 'Stężenie O₂', 'value': '93% ± 3%'},
            {'label': 'Poziom hałasu', 'value': '< 48 dB'},
        ],
        'features': ['Czujnik stężenia O₂', 'Cicha praca', 'Alarm niskiego stężenia', 'Certyfikat CE'],
    },
    {
        'category': 'tlenoterapia',
        'subcategory': 'Koncentratory Tlenu',
        'name': 'SPIRIT-3 – Przenośny Koncentrator Tlenu',
        'max_load': '',
        'short_description': 'Lekki przenośny koncentrator tlenu z trybem pulsacyjnym i baterią.',
        'long_description': (
            'SPIRIT-3 to kompaktowy przenośny koncentrator tlenu przeznaczony do aktywnego trybu życia. '
            'Akumulator w zestawie, torba transportowa, dostępne sita molekularne i filtry jako akcesoria.'
        ),
        'specs': [
            {'label': 'Tryb', 'value': 'Pulsacyjny'},
            {'label': 'Czas pracy na baterii', 'value': 'Do 4 h'},
        ],
        'features': ['Tryb pulsacyjny', 'Lekki i kompaktowy', 'Bateria w zestawie', 'Torba transportowa', 'Certyfikat CE'],
    },
    {
        'category': 'tlenoterapia',
        'subcategory': 'Pozostałe Urządzenia',
        'name': 'Nebulizator Kompresyjny TEDI',
        'short_description': 'Cichy nebulizator dla dzieci i dorosłych z kompletem masek.',
        'long_description': (
            'TEDI to kompresyjny nebulizator o cichej pracy, wyposażony w maski dla dorosłych i dzieci. '
            'Dedykowany do leczenia schorzeń górnych i dolnych dróg oddechowych.'
        ),
        'specs': [
            {'label': 'Typ', 'value': 'Kompresyjny'},
            {'label': 'Poziom hałasu', 'value': 'Cicha praca'},
        ],
        'features': ['Maska dla dziecka i dorosłego', 'Cicha praca', 'Certyfikat CE'],
    },
    {
        'category': 'tlenoterapia',
        'subcategory': 'Pozostałe Urządzenia',
        'name': 'Aparat CPAP Auto YH-690',
        'short_description': 'Automatyczny aparat CPAP do leczenia bezdechu sennego z nawilżaczem.',
        'long_description': (
            'YH-690 to Auto-CPAP z algorytmem automatycznej regulacji ciśnienia. '
            'Nawilżacz i maska w zestawie. Karta SD do zapisu danych terapii.'
        ),
        'specs': [
            {'label': 'Typ', 'value': 'Auto-CPAP'},
            {'label': 'Zakres ciśnienia', 'value': '4–20 cm H₂O'},
        ],
        'features': ['Auto-regulacja ciśnienia', 'Nawilżacz w zestawie', 'Zapis danych – karta SD', 'Certyfikat CE'],
    },
    {
        'category': 'tlenoterapia',
        'subcategory': 'Pozostałe Urządzenia',
        'name': 'Ssak Elektryczny 7E-H1',
        'short_description': 'Elektryczny ssak medyczny – stacjonarny i przenośny (7E-G1).',
        'long_description': (
            'Ssak elektryczny 7E-H1 przeznaczony do użytku stacjonarnego. '
            'Wersja przenośna 7E-G1 umożliwia użytkowanie w domu pacjenta.'
        ),
        'specs': [
            {'label': 'Model stacjonarny', 'value': '7E-H1'},
            {'label': 'Model przenośny', 'value': '7E-G1'},
        ],
        'features': ['Wersja stacjonarna i przenośna', 'Wyrób medyczny', 'Certyfikat CE'],
    },
    # ── ORTOPEDIA ────────────────────────────────────────────────────────────
    {
        'category': 'ortopedia',
        'name': 'But Marszowy Sky-Walker',
        'short_description': 'But marszowy ze stabilizacją pneumatyczną – wersja wysoka i niska.',
        'long_description': (
            'Sky-Walker to but marszowy ze stabilizacją pneumatyczną, stosowany po złamaniach, '
            'skręceniach i operacjach stawu skokowego. Dostępny w wersji niskiej (Sky-Walker Low).'
        ),
        'specs': [
            {'label': 'Stabilizacja', 'value': 'Pneumatyczna'},
            {'label': 'Wersje', 'value': 'Wysoka / Low'},
        ],
        'features': ['Stabilizacja pneumatyczna', 'Regulowany', 'Wersja niska i wysoka', 'Certyfikat CE'],
    },
    {
        'category': 'ortopedia',
        'name': 'Orteza Stawu Kolanowego GenuStrap',
        'short_description': 'Orteza kolana z regulowanymi paskami zapewniającymi stabilizację.',
        'long_description': (
            'GenuStrap zapewnia boczną stabilizację stawu kolanowego. '
            'Regulowane paski velcro umożliwiają precyzyjne dopasowanie do obwodu uda i podudzia.'
        ),
        'specs': [
            {'label': 'Staw', 'value': 'Kolanowy'},
            {'label': 'Zapięcie', 'value': 'Paski velcro'},
        ],
        'features': ['Stabilizacja boczna', 'Regulowane paski', 'Różne rozmiary', 'Certyfikat CE'],
    },
    {
        'category': 'ortopedia',
        'name': 'Orteza Stawu Skokowego MalleoTim Lite',
        'short_description': 'Lekka orteza skokowa wkładana do buta – idealna na co dzień.',
        'long_description': (
            'MalleoTim Lite to cienka orteza stawu skokowego wkładana bezpośrednio do buta. '
            'Zapewnia stabilizację boczną bez ograniczania ruchomości w płaszczyźnie strzałkowej.'
        ),
        'specs': [
            {'label': 'Staw', 'value': 'Skokowy'},
            {'label': 'Typ', 'value': 'Wkładana do buta'},
        ],
        'features': ['Lekka konstrukcja', 'Wkładana do buta', 'Stabilizacja boczna', 'Certyfikat CE'],
    },
    {
        'category': 'ortopedia',
        'name': 'Gorset Ortopedyczny / Orteza Tułowia',
        'short_description': 'Elastyczny gorset stabilizujący kręgosłup lędźwiowy z fiszbinami.',
        'long_description': (
            'Gorset ortopedyczny z panelami tylnymi wzmacniającymi i fiszbinami bocznymi. '
            'Oddychający materiał i regulowane zapięcie velcro.'
        ),
        'specs': [
            {'label': 'Obszar', 'value': 'Kręgosłup lędźwiowy'},
            {'label': 'Materiał', 'value': 'Oddychający'},
        ],
        'features': ['Fiszbiny stabilizujące', 'Regulowany', 'Oddychający materiał', 'Certyfikat CE'],
    },
    {
        'category': 'ortopedia',
        'name': 'Stabilizator Nadgarstka ManuTim Long',
        'short_description': 'Długi stabilizator nadgarstka z szyną dłoniową.',
        'long_description': (
            'ManuTim Long zapewnia unieruchomienie nadgarstka z podparciem łuku dłoni. '
            'Dedykowany przy zespole cieśni nadgarstka i po urazach.'
        ),
        'specs': [
            {'label': 'Staw', 'value': 'Nadgarstek'},
            {'label': 'Typ', 'value': 'Długi – z szyną dłoniową'},
        ],
        'features': ['Szyna dłoniowa', 'Regulowane paski', 'Prawa i lewa wersja', 'Certyfikat CE'],
    },
]


class Command(BaseCommand):
    help = 'Wypełnia bazę danych kategoriami i produktami'

    def handle(self, *args, **options):
        self.stdout.write('Tworzę kategorie...')
        cat_map = {}
        for data in CATEGORIES:
            cat, _ = Category.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'name': data['name'],
                    'icon_key': data['icon_key'],
                    'order': data['order'],
                },
            )
            cat_map[data['slug']] = cat

        self.stdout.write('Tworzę produkty...')
        for data in PRODUCTS:
            cat = cat_map[data['category']]
            Product.objects.update_or_create(
                name=data['name'],
                defaults={
                    'category': cat,
                    'subcategory': data.get('subcategory', ''),
                    'short_description': data.get('short_description', ''),
                    'long_description': data.get('long_description', ''),
                    'max_load': data.get('max_load', ''),
                    'warranty_years': data.get('warranty_years', 0),
                    'badge': data.get('badge', ''),
                    'specs': data.get('specs', []),
                    'features': data.get('features', []),
                },
            )

        total = Product.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Gotowe! Zaimportowano {total} produktów.'))
