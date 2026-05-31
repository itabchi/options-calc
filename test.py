import matplotlib.pyplot as plt
import pandas as pd

# 1. Define the data exactly as it appears in your table
data = {
    'Species': [
        'Sifrhippus sandrae', 'Mesohippus bairdi', 'Anchitherium clarencei', 
        'Parahippus leonensis', 'Archaeohippus blackbergi', 'Parahippus barbouri',
        'Calippus elachistus', 'Calippus cerasinus', 'Neohipparion trampasense',
        'Dinohippus mexicanus', 'Neohipparion eurystyle', 'Nannippus aztecus',
        'Nannippus peninsulatus', 'Equus simplicidens', 'Equus ferus'
    ],
    'HI': [
        0.48, 0.67, 0.63, 
        0.79, 1.55, 0.91, 
        2.52, 2.10, 2.25, 
        2.51, 2.61, 2.64, 
        2.73, 2.60, 2.61
    ],
    'Epoch': [
        'Eocene', 'Oligocene', 'Miocene', 
        'Miocene', 'Miocene', 'Miocene', 
        'Miocene', 'Miocene', 'Miocene', 
        'Pliocene', 'Pliocene', 'Pliocene', 
        'Pleistocene', 'Pleistocene', 'Pleistocene'
    ]
}

# 2. Create a DataFrame
df = pd.DataFrame(data)

# 3. Plotting
plt.figure(figsize=(12, 7)) # Make the figure large enough to read labels

# Plot the line and points
plt.plot(df['Species'], df['HI'], marker='o', linestyle='-', color='#2c3e50', label='Hypsodonty Index')

# 4. Formatting to make it readable
plt.xticks(rotation=45, ha='right') # Rotate species names 45 degrees
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title('Evolution of Horse Tooth Crown Height (HI) Over Time', fontsize=14)
plt.xlabel('Species (Oldest -> Youngest)', fontsize=12)
plt.ylabel('Hypsodonty Index (HI)', fontsize=12)

# Add a threshold line for Grazers vs Browsers (approx HI = 1.0)
plt.axhline(y=1.0, color='r', linestyle=':', label='Grazer Threshold (HI=1.0)')
plt.legend()

# Adjust layout to prevent cutting off labels
plt.tight_layout()

# Show the plot
plt.show()