import pandas as pd
import numpy as np

def generate_manufacturing_data(n_samples=10000):
    # Set seed for reproducibility (Member A and B will have the same data)
    np.random.seed(42)
    
    # 1. Generating Raw Features using Statistical Distributions
    data = {
        'Temperature': np.random.normal(70, 15, n_samples),      # Avg 70°C
        'Pressure': np.random.normal(50, 10, n_samples),         # Avg 50 PSI
        'Speed': np.random.normal(1500, 300, n_samples),         # RPM
        'Vibration': np.random.normal(5, 2, n_samples),          # Avg 5mm/s
        'Humidity': np.random.uniform(30, 90, n_samples),        # % Humidity
        'Power_Consumption': np.random.normal(15, 3, n_samples),  # kW
        'Material_Hardness': np.random.uniform(20, 100, n_samples),
        'Usage_Hours': np.random.uniform(10, 5000, n_samples),
        'Operator_Skill': np.random.choice([0, 1, 2], n_samples)  # 0:Junior, 1:Mid, 2:Senior
    }
    
    df = pd.DataFrame(data)
    
    # 2. Physics-Based Logic (The "Hidden Rules" for XAI to find)
    # We define Target_Quality based on interactions
    # High Speed + High Vibration + Low Material Hardness = Lower Quality
    quality_score = (
        100 
        - (df['Temperature'] * 0.1) 
        - (df['Vibration'] * df['Speed'] * 0.002) 
        - (df['Pressure'] * 0.05)
        + (df['Operator_Skill'] * 5)  # Skill improves quality
    )
    
    # Add some random noise to simulate real-world sensor error
    quality_score += np.random.normal(0, 2, n_samples)
    
    # 3. Setting the Target Labels
    df['Target_Quality'] = quality_score.round(2)
    
    # Quality_Label: 1 if Quality is low (Failure), 0 if Healthy
    # We set the threshold at the bottom 20% of quality
    threshold = np.percentile(df['Target_Quality'], 20)
    df['Failure'] = (df['Target_Quality'] < threshold).astype(int)
    
    # 4. Save to CSV
    df.to_csv('industrial_data.csv', index=False)
    
    print("--- Dataset Generation Complete ---")
    print(f"Total Samples: {n_samples}")
    print(f"Total Failures: {df['Failure'].sum()} ({df['Failure'].mean()*100:.2f}%)")
    print("File saved as: industrial_data.csv")

if __name__ == "__main__":
    generate_manufacturing_data()