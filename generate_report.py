from fpdf import FPDF
import matplotlib.pyplot as plt
from src.utils.data_loader import GameDataLoader

class ReportGenerator:
    def __init__(self):
        self.loader = GameDataLoader()
        
    def generate_pdf(self, filename='game_report.pdf'):
        """Create PDF report with key insights"""
        data = self.loader.load_raw_data()
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Video Game Sales Report', ln=1)
        
        # Add platform analysis
        self._add_platform_analysis(pdf, data)
        
        # Add genre analysis
        self._add_genre_analysis(pdf, data)
        
        pdf.output(filename)
    
    def _add_platform_analysis(self, pdf, data):
        """Add platform section to report"""
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Platform Performance', ln=1)
        
        # Generate platform chart
        plt.figure(figsize=(6, 4))
        data.groupby('Platform')['Global_Sales'].sum().plot(kind='bar')
        plt.title('Total Sales by Platform')
        plt.tight_layout()
        plt.savefig('platform_chart.png')
        plt.close()
        
        # Add to PDF
        pdf.image('platform_chart.png', x=10, w=180)
