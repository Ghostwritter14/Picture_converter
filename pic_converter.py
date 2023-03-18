import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io

with st.expander("Start Camera"):
    your_photo = st.camera_input("Camera")

# Create an Image Instance and convert
if your_photo:
    img = Image.open(your_photo)

    # Get the type of image conversion from the user
    conversion_type = st.selectbox("Select Image Conversion",
                                   ["Grayscale", "Sepia Tone", "Black and White", "Color Saturation", "Color Tint"])

    # Perform the selected image conversion
    if conversion_type == "Grayscale":
        converted_img = img.convert("L")
    elif conversion_type == "Sepia Tone":
        converted_img = img.convert("RGB")
        converted_img = Image.blend(converted_img, Image.new('RGB', converted_img.size, (244, 229, 183)), 0.5)
    elif conversion_type == "Black and White":
        converted_img = img.convert("1")
    elif conversion_type == "Color Saturation":
        saturation_level = st.slider("Color Saturation Level", 0, 200, 100, 5)
        converted_img = ImageEnhance.Color(img).enhance(saturation_level / 100)
    elif conversion_type == "Color Tint":
        tint_color = st.selectbox("Color Tint", ["Red", "Green", "Blue"])
        if tint_color == "Red":
            tinted_img = ImageOps.colorize(img.convert("L"), "#ff0000", "#000000")
        elif tint_color == "Green":
            tinted_img = ImageOps.colorize(img.convert("L"), "#00ff00", "#000000")
        elif tint_color == "Blue":
            tinted_img = ImageOps.colorize(img.convert("L"), "#0000ff", "#000000")
        converted_img = tinted_img.convert("RGB")

    st.image(converted_img, caption=f"{conversion_type} Image")

    # Add a button to download the converted image as a PNG file
    if st.button("Download Image"):
        # Convert the image to bytes and save it to a BytesIO object
        img_bytes = io.BytesIO()
        converted_img.save(img_bytes, format="PNG")
        # Download the BytesIO object as a file
        st.download_button(
            label="Download Image",
            data=img_bytes.getvalue(),
            file_name=f"{conversion_type}_image.png",
            mime="image/png"
        )




