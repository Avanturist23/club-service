import pytest
from app.api.models import ClubIn, ClubOut

clubs = ClubIn(
    name='Бильярд Москва',
    phone='+71987654321',
    count_users='1500',
    country='Россия'
)


def test_create_client(clubs: ClubIn = clubs):
    assert dict(clubs) == {'name': clubs.name,
                              'phone': clubs.phone,
                              'count_users': clubs.count_users,
                              'country': clubs.country
                              }


def test_update_client_age(clubs: ClubIn = clubs):
    clubs_upd = ClubOut(
        name='Бильярд Москва',
        phone='+71987654321',
        count_users='1500',
        country='Россия',
        id=1
    )
    assert dict(clubs_upd) == {'name': clubs.name,
                              'phone': clubs.phone,
                              'count_users': clubs.count_users,
                              'country': clubs.country,
                              'id': clubs_upd.id
                              }


def test_update_client_genre(clubs: ClubIn = clubs):
    clubs_upd = ClubOut(
        name='Бильярд Москва',
        phone='+71987654321',
        count_users='1500',
        country='Россия',
        id=1
    )
    assert dict(clubs_upd) == {'name': clubs.name,
                              'phone': clubs.phone,
                              'count_users': clubs.count_users,
                              'country': clubs.country,
                              'id': clubs_upd.id
                              }
