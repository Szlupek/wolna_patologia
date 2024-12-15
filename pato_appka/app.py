import datetime
import os
import random

import psycopg2
from flask import Flask, render_template, request

from conf.priv import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME

app = Flask(__name__)

# Path to the folder containing images
IMAGE_FOLDER = os.path.expanduser("~/Share/images_renamed")

connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
)
cursor = connection.cursor()


@app.route("/")
def index():
    """
    Serve the main page of the web application.

    This route performs the following actions:
    1. Retrieves a list of image files from the `IMAGE_FOLDER` directory, filtering
       for files with extensions `.png`, `.jpg`, `.jpeg`, or `.gif`.
    2. Captures the visitor's IP address and the current timestamp.
    3. If no images are available, renders the `index.html` template with a message
       indicating no images are available.
    4. If images are found:
       - Randomly selects an image from the list.
       - Logs the visitor's IP address, the current timestamp, and the selected image
         into the database table `visitor_ip`.
       - Renders the `index.html` template, passing the URL and name of the selected
         image, along with the visitor's IP address.

    Returns:
        str: Rendered HTML content of the `index.html` template.
    """
    # Get a list of image files
    images = [
        img
        for img in os.listdir(IMAGE_FOLDER)
        if img.endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    visitor_ip = str(request.remote_addr)
    now = str(datetime.datetime.now())

    if not images:
        return render_template(
            "index.html", image_url=None, image_name="No images available!"
        )

    # Pick a random image
    random_image = str(random.choice(images))
    cursor.execute(
        f"""
        INSERT INTO visitor_ip(ip, time, car) 
        VALUES('{visitor_ip}','{now}','{random_image}')
        """
    )
    connection.commit()
    return render_template(
        "index.html",
        image_url=f"/static/{random_image}",
        image_name=random_image.split(".")[0],
        ip=visitor_ip,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
