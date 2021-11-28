import instaloader


class Instagram:
    
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.__non_followers = []

    def __login_loader(self):
        loader = instaloader.Instaloader()
        loader.login(self.username, self.password)
        return loader


    def __get_profile(self):
        profile = instaloader.Profile.from_username(self.__login_loader().context, self.username)
        return profile


    def get_followers(self, profile):
        followers = []
        for follower in profile.get_followers():
            followers.append(follower.username)
        return followers

    def get_followings(self, profile):
        followings = []
        for following in profile.get_followees():
            followings.append(following.username)
        return followings

    @property
    def get_non_followers(self):
        return self.__non_followers

    def find_non_followers(self):
        profile = self.__get_profile()
        self.__non_followers = set(self.get_followings(profile)) - set(self.get_followers(profile))
        self.write_to_file("unfollowers.txt", self.__non_followers)

    def write_to_file(self, text_name: str, list_to_write: list):
        with open(text_name, 'w') as f:
            for el in list_to_write:
                f.write(f"{el}\n")