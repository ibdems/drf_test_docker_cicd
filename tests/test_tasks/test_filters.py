import pytest

from tasks.filters import TaskFilter
from tasks.models import Task

@pytest.mark.django_db
def test_TastFilter_custom_level(tasks_data):
    filter_set = TaskFilter(
        {'custom_level': 5},
        queryset=Task.objects.all()
    )

    filter_result = filter_set.qs

    filter_test = Task.objects.filter(completed=False, level__gt=5)

    assert list(filter_result) == list(filter_test)

@pytest.mark.django_db
def test_TaskFilter_get_ordering(tasks_data):
    filter_set_desc = TaskFilter(
        {'ordering':'publicated_at'},
        queryset=Task.objects.all()
    )
    filter_set_asc = TaskFilter(
        {'ordering':'publicated_at'},
        queryset=Task.objects.all()
    )
    filter_desc_result = filter_set_desc.qs
    filter_asc_result = filter_set_desc.qs
    filter_test_desc = Task.objects.order_by('created_at')
    filter_test_asc = Task.objects.order_by('created_at')

    assert list(filter_desc_result) == list(filter_test_desc)
    assert list(filter_asc_result) == list(filter_desc_result)
