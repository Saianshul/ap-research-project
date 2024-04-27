from PIL import Image, ImageSequence, ImageEnhance

def modify_first_frame(frame):
    frame = frame.resize((500, 500))
    frame = frame.rotate(-60)
    cropped_region = frame.crop((50, 50, 100, 100))
    cropped_region = cropped_region.transpose(Image.ROTATE_180)  # Corrected
    frame.paste(cropped_region, (50, 50, 100, 100))
    frame = ImageEnhance.Contrast(frame).enhance(5.0)

    return frame

def modify_second_frame(frame):
    bands = frame.split()
    mask = bands[0].point(lambda p: p < 200 and 255)
    processed_blue_band = bands[2].point(lambda i: i * 1.5)
    bands[2].paste(processed_blue_band, None, mask)
    frame = Image.merge('RGB', bands)  # Corrected

    return frame

original_gif = Image.open('original.gif')

frames = []
for frame in ImageSequence.Iterator(original_gif):
    frames.append(frame.copy())

frames[0] = modify_first_frame(frames[0])
frames[1] = modify_second_frame(frames[1])

frames[0].save('modified1.gif', format='GIF', append_images=frames[1:], save_all=True, loop=0, duration=original_gif.info['duration'])