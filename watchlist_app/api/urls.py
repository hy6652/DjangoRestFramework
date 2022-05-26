from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import StreamPlaformAV, StreamDetailAV, WatchListAV, WatchDetailAV, ReviewList, ReviewDetail, ReviewCreate

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlaformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream-detail'),

    # path('review/', ReviewList.as_view(), name='stream-detail'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    # strea/1/reivew 와 같이 사용하면, 마 stream 중에서 pk가 1에 해당하는 모든 review를 보여주는 것 같지만, 사실 이건 pk에 해당하는 watchlist의 review 전체를 보여준다.
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
