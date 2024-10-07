# Clean and rename columns for easier processing
df_cleaned = df.rename(columns={
    'PLANILHA DE ACOMPANHAMENTO - ASSISTÊNCIA FARMACÊUTICA – ANALISES DE INTERAÇÕES FXF': 'Data',
    'Unnamed: 1': 'Paciente',
    'Unnamed: 2': 'Idade',
    'Unnamed: 3': 'Sexo',
    'Unnamed: 4': 'Setor',
    'Unnamed: 5': 'Prescricao_Interacao',
    'Unnamed: 6': 'Interacoes_Graves',
    'Unnamed: 7': 'Intervencao_Realizada',
    'Unnamed: 8': 'Intervencao_Aceita',
    'Unnamed: 9': 'Quantas_Aceitas'
})

# Drop the first row as it contains the column headers
df_cleaned = df_cleaned.drop(0)

# Convert columns to appropriate data types
df_cleaned['Idade'] = pd.to_numeric(df_cleaned['Idade'], errors='coerce')
df_cleaned['Interacoes_Graves'] = pd.to_numeric(df_cleaned['Interacoes_Graves'], errors='coerce')
df_cleaned['Quantas_Aceitas'] = pd.to_numeric(df_cleaned['Quantas_Aceitas'], errors='coerce')

# General overview: basic statistics
overview = df_cleaned.describe()

# Count total number of interactions and interventions
total_interactions = df_cleaned['Interacoes_Graves'].sum()
total_interventions = df_cleaned['Intervencao_Realizada'].str.contains('Sim', na=False).sum()
total_accepted_interventions = df_cleaned['Intervencao_Aceita'].str.contains('Sim', na=False).sum()

overview, total_interactions, total_interventions, total_accepted_interventions
