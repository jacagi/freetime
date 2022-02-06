import instaloader


def main():
    L = instaloader.Instaloader()
    username = "user"
    password = "pass"
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, username)
    follow_list = list(set(profile.get_followees()) - set(profile.get_followers()))
    for f in follow_list: print(f.username)

if __name__ == "__main__":
    main()