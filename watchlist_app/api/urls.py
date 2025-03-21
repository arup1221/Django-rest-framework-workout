from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (
    StreamPlatformAV, WatchListAV, WatchDetailAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS, UserReview, WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS,
                basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),name='streamplatform-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list2'),

    # path('review/',ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>',  ReviewDetail.as_view(), name="review-detail"),


    path('<int:pk>/review-create/',
         ReviewCreate.as_view(), name='review-create'),

    path('<int:pk>/reviews/', ReviewList.as_view(),
         name='review-list'),  # all the review for a particular movie [streamplatform-detail]
    path('review/<int:pk>/',  ReviewDetail.as_view(),
         name="review-detail"),  # do access individual review
    #     path('reviews/<str:username>/', UserReview.as_view(), name="user-review"),
    path('reviews/', UserReview.as_view(), name="user-review"),
    
]
