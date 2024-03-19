from instaloader import Instaloader
from instaloader import Profile
from instaloader import FrozenNodeIterator
import os
import sys
import json
import time
import random
import datetime
import configparser


class PostAlreadyDownloaded(Exception):
    pass


class DownloadSaved:
    def __init__(self, root=os.getcwd(), folder="saved"):
        self.root = root
        self.is_to_be_organized = False
        os.chdir(self.root)

        self.folder = folder
        self.get_credentials()

        # Trying to avoid 400 ERROR and account locking.
        self.remove_session()

        self.L = Instaloader(
            save_metadata=False,
            compress_json=False,
            download_comments=False,
            post_metadata_txt_pattern="",
            filename_pattern="{date_utc:%Y-%m-%d}_{profile}_{shortcode}",
        )

        self.set_login()
        self.profile = Profile.from_username(self.L.context, self.USER)

    def get_credentials(self):
        configpath = os.path.join(self.root, "config.ini")

        if not os.path.exists(configpath):
            config = configparser.ConfigParser()
            time.sleep(2)
            config["ig"] = {
                "username": input("Username: "),
                "password": input("Password: "),
            }

            with open(configpath, "w") as file:
                config.write(file)

            self.USER = config["ig"]["username"]
            self.PASSWORD = config["ig"]["password"]
        else:
            config = configparser.ConfigParser()
            config.read(configpath)

            self.USER = config["ig"]["username"]
            self.PASSWORD = config["ig"]["password"]

    def set_login(self):
        session_filename = f"session-{self.USER}"
        session_filepath = os.path.join(self.root, session_filename)

        if not os.path.exists(session_filepath):
            self.L.login(self.USER, self.PASSWORD)
            self.L.save_session_to_file(filename=session_filename)
        else:
            self.L.load_session_from_file(self.USER, filename=session_filepath)

    def download(self):
        current_time = round(time.time())

        freeze_filename = "resume.json"
        freeze_filepath = os.path.join(self.root, freeze_filename)

        saved_posts = self.profile.get_saved_posts()

        if os.path.exists(freeze_filepath):
            print(">> Back from where it stopped...")
            print(" ")

            with open(freeze_filepath) as f:
                saved_posts.thaw(FrozenNodeIterator(*json.load(f)))

        try:
            for self.count, post in enumerate(saved_posts):
                time_sleep_lvl_1 = 40 + random.randint(20, 80)
                time_sleep_lvl_2 = 480 + random.randint(60, 180)
                time_sleep_lvl_3 = 3000 + random.randint(100, 700)

                if (self.count + 1) == 200:
                    json.dump(saved_posts.freeze(), open(freeze_filepath, "w"))

                    print(" ")
                    print(">> 200 Posts downloaded! Stopping...")
                    break

                elif (self.count + 1) % 100 == 0:
                    self.check_existence(self.L.download_post(post, self.folder))
                    json.dump(saved_posts.freeze(), open(freeze_filepath, "w"))

                    print(" ")
                    print(
                        f">> 100 Posts downloaded. Waiting {time_sleep_lvl_3} seconds!"
                    )
                    time.sleep(time_sleep_lvl_3)

                elif (self.count + 1) % 10 == 0:
                    self.check_existence(self.L.download_post(post, self.folder))
                    json.dump(saved_posts.freeze(), open(freeze_filepath, "w"))

                    print(" ")
                    print(
                        f">> 10 Posts downloaded. Waiting {time_sleep_lvl_2} seconds!"
                    )
                    time.sleep(time_sleep_lvl_2)

                else:
                    self.check_existence(self.L.download_post(post, self.folder))

                    print(f">> Waiting {time_sleep_lvl_1} seconds!")
                    time.sleep(time_sleep_lvl_1)

        except KeyboardInterrupt:
            json.dump(saved_posts.freeze(), open(freeze_filepath, "w"))

        except PostAlreadyDownloaded:
            json.dump(saved_posts.freeze(), open(freeze_filepath, "w"))
            os.rename(freeze_filename, f"{current_time}_{freeze_filename}")
            print(">> All new posts downloaded!")
            folder = os.path.join(self.root, "saved")
            # if self.is_to_be_organized:
            #    _ = FileOrganizer(folder, by="month", keep_last=True, only_root=True)

        except Exception as e:
            json.dump(saved_posts.freeze(), open(freeze_filepath, "w"))
            print(">> Something went wrong.")
            print(e)

    def check_existence(self, downloaded):
        if not downloaded and self.count > 0:
            raise PostAlreadyDownloaded

    def remove_session(self):
        session_file = f"session-{self.USER}"
        session_path = os.path.join(self.root, session_file)

        if os.path.exists(session_path):
            os.remove(session_path)


def main():
    saved = DownloadSaved(root=os.getcwd(), folder="saved")
    saved.download()


if __name__ == "__main__":
    main()