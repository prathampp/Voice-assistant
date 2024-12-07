import os


def open_app(app_name):
    app_paths = {
        "facetime": "/System/Applications/FaceTime.app",
        "vlc": "/path/to/VLC.app",
        "safari": "/path/to/Safari.app",


    }

    if app_name.lower() in app_paths:
        os.system(f"open {app_paths[app_name.lower()]}")
        return f"Opening {app_name}..."
    else:
        return f"Sorry, I can't open {app_name}."
#bmmxm