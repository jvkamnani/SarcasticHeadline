from flask import Flask, render_template, request
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text



model = tf.keras.models.load_model('model/colab_model.h5', custom_objects={'KerasLayer':hub.KerasLayer})


def predict_sarcastic_headline(headline):


    
    pred=model.predict(headline)[0][0]
    if(pred>0.5):
        result=True
    else:
        result=False
    print(result)
    return result


app = Flask(__name__) 

@app.route('/', methods=['POST', 'GET'])
def predict_site():
    messages = {}
    if request.method == 'GET':
        return render_template('project_page.html')
    if request.method == 'POST':
        messages['answer'] = predict_sarcastic_headline([request.form['headline']])
        
    return render_template('project_page.html', messages=messages)

if __name__ == '__main__':
    app.run(debug = True)


