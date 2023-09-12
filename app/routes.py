from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    books = [
        {
            'author':'Etaf Rum',
            'title':'Evil Eye',
            'desсription': 'After Yara is placed on probation at work for fighting with a racist coworker, her Palestinian mother claims the provocation and all that\'s come after were the result of a family curse. While Yara doesn\'t believe in old superstitions, she finds herself unpacking her strict, often volatile childhood growing up in Brooklyn, looking for clues as to why she feels so unfulfilled in a life her mother could only dream of. Etaf Rum\'s follow-up to her 2019 debut, A Woman Is No Man, is a complicated mother-daughter drama that looks at the lasting effects of intergenerational trauma and what it takes to break the cycle of abuse.',
            'publisher':'Harper',
            'publish_date':'05.09.2023',
            'language':'English',
            'genre':'romantic',
            'price':'27.00',
            'pages':'352',
            'type':'Hardcover',
            'uen_upc':'9780062987907'
        },
        {
            'author':'Stephen King',
            'title':'Holly',
            'desсription': 'Stephen King is the author of more than sixty books, all of them worldwide bestsellers. His recent work includes Holly, Fairy Tale, Billy Summers, If It Bleeds, The Institute, Elevation, The Outsider, Sleeping Beauties (cowritten with his son Owen King), and the Bill Hodges trilogy: End of Watch, Finders Keepers, and Mr. Mercedes (an Edgar Award winner for Best Novel and a television series streaming on Peacock). His novel 11/22/63 was named a top ten book of 2011 by The New York Times Book Review and won the Los Angeles Times Book Prize for Mystery/Thriller. His epic works The Dark Tower, It, Pet Sematary, Doctor Sleep, and Firestarter are the basis for major motion pictures, with It now the highest-grossing horror film of all time. He is the recipient of the 2020 Audio Publishers Association Lifetime Achievement Award, the 2018 PEN America Literary Service Award, the 2014 National Medal of Arts, and the 2003 National Book Foundation Medal for Distinguished Contribution to American Letters. He lives in Bangor, Maine, with his wife, novelist Tabitha King',
            'publisher':'Harper',
            'publish_date':'05.09.2023',
            'language':'English',
            'genre':'romantic',
            'price':'27.00',
            'pages':'352',
            'type':'Hardcover',
            'uen_upc':'9780062987907'
        },
    ]	
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user, books=books)