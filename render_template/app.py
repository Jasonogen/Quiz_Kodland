from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Güvenlik için kullanılacak secret key

# Basit bir puanlama sistemini simüle eden bir sözlük
correct_answers = {
    'color': 'Red',
    'animal': 'Cat'
}

@app.route('/', methods=['GET'])
def quiz():
    if 'best_score' not in session:
        session['best_score'] = 0
    return render_template('quiz.html', 
                           best_score=session['best_score'],
                           color_options=['Red', 'Blue', 'Green'],
                           animal_options=['Dog', 'Cat', 'Parrot'])

@app.route('/submit', methods=['POST'])
def submit_quiz():
    # Puanını hesaplamak için yaptım
    score = 0
    for question, answer in correct_answers.items():
        if request.form.get(question) == answer:
            score += 50  # Her doğru cevap 50 puan olsun

    # En yüksek puanı yazdır
    if score > session.get('best_score', 0):
        session['best_score'] = score

    # Yönlendirme için. Sonuçlar sayfasına yönlendir
    return redirect(url_for('results', score=score))

@app.route('/results')
def results():
    score = request.args.get('score', 0)
    return f'Your score: {score}%.<br> <a href="/">Try again?</a>'

if __name__ == '__main__':
    app.run(debug=True)
