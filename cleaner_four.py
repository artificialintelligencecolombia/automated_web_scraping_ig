import pandas as pd
import re

def clean_dataset(file_path):
    """
    Clean and standardize categories and countries in the Excel dataset,
    ensuring no duplicates in categorization.
    """
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Drop completely empty rows
    df = df.dropna(how='all')
    
    # First, replace empty strings with NaN
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    
     # Convert boolean columns to yes/no
    bool_columns = df.select_dtypes(include=['bool']).columns
    for col in bool_columns:
        df[col] = df[col].map({True: 'yes', False: 'no'})
    
    
    # Comprehensive category standardization mapping
    category_mapping = {
        # Food and Kitchen
        r'(alimentos\s*saludables|artículos\s*\*\s*cocina)': 'comidas & cocina',
        
        # Fashion and Accessories
        r'bolsos': 'moda & accesorios',
        r'calzado': 'moda & accesorios',
        r'cuidado\s*\*\s*piel': 'salud',
        r'ropa': 'moda & accesorios',
        r'(ropa\s*deportiva|fitness)': 'moda & accesorios',
        r'(accesorios\s*\*\s*joyería|relojes)': 'moda & accesorios',
        
        # Supplements and Health
        r'suplementos': 'salud',
        r'(perfumes|fragancias)': 'beauty',
        r'(belleza\s*\*\s*maquillaje|cosméticos)': 'cosmeticos',
        
        # Technology and Electronics
        r'(accesorios\s*\*\s*smartphones|tecnología|dispositivos)': 'tecnologia',
        
        # Home and Decoration
        r'(decoracion\s*\*\s*hogar|mobiliario)': 'hogar',
        
        # Toys and Hobbies
        r'(juguetes\s*\*\s*niños|hobbies)': 'juguetes & juegos',
        
        # Travel and Services
        r'(turismo|agencia\s*\*\s*viajes)': 'servicios',
        r'(marketing|publicidad|mercadeo)': 'servicios',
        
        # New category for Pets
        r'(productos\s*\*\s*mascotas|mascotas)': 'mascotas',
        
        # Retain previous mappings if still relevant
        r'(moda mujer|moda hombre|fashion)': 'moda & accesorios',
        r'(ropa\s*AND\s*accesorios|clothing)': 'moda & accesorios',
    }
    
    # Comprehensive country standardization mapping
    country_mapping = {
        r'(Argentina|Buenos\s*Aires|Arg)': 'Argentina',
        r'(Bolivia|La\s*Paz|Bo)': 'Bolivia',
        r'(Chile|Santiago|Cl)': 'Chile',
        r'(Colombia|Bogotá|Col)': 'Colombia',
        r'(Ecuador|Quito|Ec)': 'Ecuador',
        r'(España|Madrid|Espana)': 'Espana',
        r'(Guatemala|Gt)': 'Guatemala',
        r'(México|Mexico|mx)': 'Mexico',
        r'(Panamá|Panama|Pa)': 'Panama',
        r'(Paraguay|Asunción|Py)': 'Paraguay',
        r'(Perú|Peru|Lima|Pe)': 'Peru',
        r'(República\s*Dominicana|Republica\s*Dominicana|Santo\s*Domingo)': 'Republica Dominicana',
        r'(Uruguay|Montevideo|Uy)': 'Uruguay',
        'Chile': 'Chile',
        'Colombia': 'Colombia',
        'Costa Rica': 'Costa Rica',
        'Ecuador': 'Ecuador',
        'Paraguay': 'Paraguay'
    }

    def standardize_value(value, mapping):
        """Standardize a value using regex mapping"""
        if pd.isna(value) or not isinstance(value, str):
            return pd.NA
            
        value = value.lower().strip()
        
        # Try each pattern in the mapping
        for pattern, standardized in mapping.items():
            if re.search(pattern, value, re.IGNORECASE):
                return standardized
                
        return value

    # Apply standardization
    if 'category' in df.columns:
        df['category'] = df['category'].apply(lambda x: standardize_value(x, category_mapping))
        
    if 'country' in df.columns:
        df['country'] = df['country'].apply(lambda x: standardize_value(x, country_mapping))
    
    # Remove duplicates based on all columns
    df = df.drop_duplicates()
    
    # Sort values by category and country for better organization
    df = df.sort_values(['category', 'country'], na_position='last')
    
    # Reset index after all operations
    df = df.reset_index(drop=True)
    
    return df

def analyze_standardization(df):
    """Analyze the results of standardization"""
    print("\nStandardization Summary:")
    
    # Print boolean columns conversion
    bool_like_columns = [col for col in df.columns if df[col].isin(['yes', 'no']).any()]
    if bool_like_columns:
        print("\nBoolean Columns converted to yes/no:")
        for col in bool_like_columns:
            yes_count = (df[col] == 'yes').sum()
            no_count = (df[col] == 'no').sum()
            print(f"- {col}: yes={yes_count}, no={no_count}")
    
    print("\nUnique Categories:")
    categories = sorted([cat for cat in df['category'].unique() if pd.notna(cat)])
    for cat in categories:
        print(f"- {cat}")
        
    print("\nUnique Countries:")
    countries = sorted([country for country in df['country'].unique() if pd.notna(country)])
    for country in countries:
        print(f"- {country}")
        
    print(f"\nTotal unique category-country combinations: {len(df)}")
    
    # Print counts for each category
    print("\nCategory Counts:")
    print(df['category'].value_counts(dropna=False))
    
    # Print counts for each country
    print("\nCountry Counts:")
    print(df['country'].value_counts(dropna=False))

def main():
    try:
        # Replace with your file path
        file_path = './prefinal4.xlsx'
        
        # Read and clean the data
        print("Reading and cleaning data...")
        cleaned_df = clean_dataset(file_path)
        
        # Save cleaned data
        output_path = 'final_dataset4.xlsx'
        cleaned_df.to_excel(output_path, index=False)
        print(f"\nCleaned dataset saved to {output_path}")
        
        # Analyze results
        analyze_standardization(cleaned_df)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise  # This will show the full error traceback

if __name__ == "__main__":
    main()