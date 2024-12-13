import os
import random
from flask import Flask, render_template

app = Flask(__name__)

# Path to the folder containing images
IMAGE_FOLDER = os.path.expanduser("~/Share/images_renamed")

@app.route("/")
def index():
    # Get a list of image files
    images = [img for img in os.listdir(IMAGE_FOLDER) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if not images:
        return render_template("index.html", image_url=None, image_name="No images available!")
    
    # Pick a random image
    random_image = random.choice(images)
    return render_template("index.html", image_url=f"/static/{random_image}", image_name=random_image.split('.')[0])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
