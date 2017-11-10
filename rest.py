from flask import Flask, render_template, redirect
import json
import urllib2

app = Flask(__name__)

def get_image_url(index):
    data = urllib.urlopen('https://dscovr.gsfc.nasa.gov/api/natural?api_key=jrrseOvLIYK1RZQM7l3uVWGfP64mZysSUKs0LzR6')
    data = json.loads(data.read())

    im = data[index]['image']
    
    date = data[index]['date']
    date = '/'.join(date.split('-'))[:10]

    im_url = 'https://dscovr.gsfc.nasa.gov/archive/natural/' + date + '/png/' + im + '.png'

    caption = data[index]['caption']
    
    return im_url, caption


@app.route('/')
def root():
    im_url_1, cap_1 = get_image_url(0)
    im_url_2, cap_2 = get_image_url(5)
    #return redirect(im_url_2)
    return render_template('image.html', image_1_url=im_url_1, caption_1=cap_1, image_2_url=im_url_2, caption_2=cap_2)

if __name__ == '__main__':
    app.debug == True
    app.run()
