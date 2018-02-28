import os

p5_base = "https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.6.0"

modules = [
    (p5_base + "/p5.js", "p5.js"),
    (p5_base + "/addons/p5.dom.min.js", "p5.dom.min.js"),
    (p5_base + "/addons/p5.sound.min.js", "p5.sound.min.js"),

    ("https://code.jquery.com/jquery-3.3.1.min.js", "jquery-3.3.1.min.js")
]


def download_modules():
    if not os.path.exists("modules"):
        os.makedirs("modules")

    for url, filename in modules:
        path = "modules/{}".format(filename)
        dl_cmd = "curl {} > {}".format(url, path)

        print(dl_cmd)
        os.system(dl_cmd)


if __name__ == "__main__":
    download_modules()
