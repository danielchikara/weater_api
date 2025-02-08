import psycopg2

#este script  solo puede ejecutarse una vez

# Conexión a la base de datos PostgreSQL
def connect_db():
    return psycopg2.connect(
        host="localhost",  
        database="leads_db",   
        user="postgres",  # Cambia por tu usuario
        password="tu_password"  # aqui debes cambiar por tu contraseña
    )

# Función para insertar leads en la tabla
def insert_leads():
    leads = [
        {"id": 1, "name": "Ana Salcedo", "location": "Medellín", "budget": 2000000},
        {"id": 2, "name": "Santiago Gallo", "location": "Medellín", "budget": 5000000},
        {"id": 3, "name": "Carlota Habib", "location": "Medellín", "budget": 6500000},
        {"id": 4, "name": "Pablo Sánchez", "location": "Bogotá", "budget": 3500000},
        {"id": 5, "name": "Andrés Arias", "location": "Bogotá", "budget": 1500000},
        {"id": 6, "name": "Andrés Limas", "location": "Bogotá", "budget": 4500000},
    ]

    conn = connect_db()
    cursor = conn.cursor()

    for lead in leads:
        cursor.execute("""
            INSERT INTO leads (id, name, location, budget)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (lead["id"], lead["name"], lead["location"], lead["budget"]))

    conn.commit()
    cursor.close()
    conn.close()

# Función para filtrar leads
def filter_leads(location=None, min_budget=None, max_budget=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM leads WHERE TRUE"
    params = []

    if location:
        query += " AND location = %s"
        params.append(location)

    if min_budget is not None:
        query += " AND budget >= %s"
        params.append(min_budget)

    if max_budget is not None:
        query += " AND budget <= %s"
        params.append(max_budget)

    cursor.execute(query, params)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results

# Función para calcular el presupuesto total
def calculate_total_budget(leads):
    return sum(lead[3] for lead in leads)  # El presupuesto está en la columna 3

# Función para ordenar leads por presupuesto
def sort_leads(leads):
    return sorted(leads, key=lambda x: x[3], reverse=True)

# Función principal para presentar resultados
def main():
    # 1. Inserta leads en la base de datos
    insert_leads()

    # 2. Filtra leads (por ejemplo, ubicación: "Medellín", presupuesto mayor a 3000000)
    filtered_leads = filter_leads(location="Medellín", min_budget=3000000)

    # 3. Calcula el presupuesto total
    total_budget = calculate_total_budget(filtered_leads)

    # 4. Ordena los leads por presupuesto (de mayor a menor)
    sorted_leads = sort_leads(filtered_leads)

    # 5. Presenta los resultados
    print("Leads filtrados y ordenados:")
    for lead in sorted_leads:
        print(f"ID: {lead[0]}, Nombre: {lead[1]}, Ciudad: {lead[2]}, Presupuesto: {lead[3]}")

    print(f"\nPresupuesto total: {total_budget}")

# Ejecuta el script
if __name__ == "__main__":
    main()
