from flask import Flask, render_template
import plotly.express as px
import pandas as pd
from src.utils.data_loader import GameDataLoader

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Load and prepare data
    loader = GameDataLoader()
    data = loader.load_raw_data()
    
    # Create visualizations
    fig1 = px.bar(data.groupby('Platform')['Global_Sales'].sum().reset_index(), 
                 x='Platform', y='Global_Sales', title='Sales by Platform')
    
    fig2 = px.scatter(data, x='Critic_Score', y='Global_Sales', 
                     color='Genre', title='Scores vs Sales')
    
    return render_template('dashboard.html', 
                         plot1=fig1.to_html(),
                         plot2=fig2.to_html())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
