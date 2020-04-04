from django.urls import path

from api.views import get_all_companies, get_company, get_company_vacancies, get_vacancies, get_vacancy, get_vacancy_top_ten

urlpatterns = [
    path('companies/', get_all_companies),
    path('companies/<int:company_id>', get_company),
    path('companies/<int:company_id>/vacancies', get_company_vacancies),
    path('vacancies/', get_vacancies),
    path('vacancies/<int:vacancy_id>', get_vacancy),
    path('vacancies/top-ten', get_vacancy_top_ten)
]