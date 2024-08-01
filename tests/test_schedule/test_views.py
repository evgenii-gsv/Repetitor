import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


class TestAppointmentViews:

    @pytest.mark.db
    def test_list(self, client, user, second_user):
        url = reverse('appointment-list')

        # unauthenticated requests
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        # authenticated requests
        client.force_authenticate(user=user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

        # creating appointments
        baker.make('schedule.Appointment', schedule=user.schedule, start='2024-07-25T13:00', end='2024-07-25T14:00')
        baker.make('schedule.Appointment', schedule=user.schedule, start='2024-07-25T14:00', end='2024-07-25T15:00')
        baker.make(
            'schedule.Appointment', schedule=second_user.schedule, start='2024-07-25T13:00', end='2024-07-25T14:00'
        )

        response = client.get(url)
        assert len(response.data) == 2

    @pytest.mark.db
    def test_create(self, client, user):
        url = reverse('appointment-list')
        client.force_authenticate(user=user)

        # success
        response = client.post(url, {
            'start': '2024-07-25T12:00',
            'end': '2024-07-25T13:00',
        }, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['start'] == '2024-07-25T12:00:00Z'
        assert response.data['end'] == '2024-07-25T13:00:00Z'

        # validation errors
        response = client.post(url, {
            'start': '2024-07-25T11:30',
            'end': '2024-07-25T12:30',
        }, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response = client.post(url, {
            'start': '2024-07-25T12:30',
            'end': '2024-07-25T13:30',
        }, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response = client.post(url, {
            'start': '2024-07-25T18:00',
            'end': '2024-07-25T17:00',
        }, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response = client.get(url)
        assert len(response.data) == 1

    @pytest.mark.db
    def test_retrieve(self, client, user, second_user):
        my_appointment = baker.make('schedule.Appointment', schedule=user.schedule)
        not_my_appointment = baker.make('schedule.Appointment', schedule=second_user.schedule)
        client.force_authenticate(user=user)

        response = client.get(my_appointment.get_absolute_url())
        assert response.status_code == status.HTTP_200_OK

        response = client.get(not_my_appointment.get_absolute_url())
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.db
    def test_update(self, client, user):
        appointment = baker.make(
            'schedule.Appointment', schedule=user.schedule, start='2024-07-25T13:00', end='2024-07-25T14:00'
        )
        client.force_authenticate(user=user)

        response = client.put(
            appointment.get_absolute_url(), {
                'start': '2024-07-25T13:30',
                'end': '2024-07-25T14:00'
            }, format='json'
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['start'] == '2024-07-25T13:30:00Z'

        response = client.patch(appointment.get_absolute_url(), {'end': '2024-07-25T14:30'}, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['end'] == '2024-07-25T14:30:00Z'

    @pytest.mark.db
    def test_delete(self, client, user):
        appointment = baker.make(
            'schedule.Appointment', schedule=user.schedule, start='2024-07-25T13:00', end='2024-07-25T14:00'
        )
        client.force_authenticate(user=user)

        response = client.delete(appointment.get_absolute_url())
        assert response.status_code == status.HTTP_204_NO_CONTENT
