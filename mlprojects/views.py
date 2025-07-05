from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score

def rain(request):
    df = pd.read_csv('data.csv')
    x = df[['temp','humidity','ph']]
    y = df['rain']

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    result = r2_score(y_test, y_pred)
    #print('R2 Score:', result)

    p = None
    if request.method=='POST':
        a = request.POST.get('temp')
        b = request.POST.get('humidity')
        c = request.POST.get('ph')
        # Convert to numbers
        p = model.predict([[float(a), float(b), float(c)]])[0]

        return render(request, 'mlproject.html', {'result': p})
    return render(request,'mlproject.html')