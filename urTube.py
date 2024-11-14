import user
from user import *
from video import Video
from time import sleep


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None



    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        if len(self.users) == 0:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            if self.log_in(new_user.nickname, new_user.password):
                self.current_user = new_user
        else:
            for user in self.users:
                if user.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    return
                else:
                    new_user = User(nickname, password, age)
                    self.users.append(new_user)
                    if self.log_in(new_user.nickname, new_user.password):
                        self.current_user = new_user
                    return

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word: str):
        search_word = search_word.lower()
        matching_videos = [video.title for video in self.videos if search_word in video.title.lower()]
        return matching_videos

    def watch_video(self, name_video: str):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if name_video.lower() in video.title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(1, 11):
                        print(i, end='')
                        sleep(1)
                    print(" Конец видео")
                return
        return