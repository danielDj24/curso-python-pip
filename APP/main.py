import utils
import read_csv
import charts
import pandas as pd # libreria que filtra datos, lee csv 


def run():
  '''
  
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country'],data))
  percentages = list(map(lambda x: x['World Population Percentage'],data))
'''  # llama la funcion que lee el csv de forma manual

  
  
  #data frames (datos de donde obtenemos info)
  df= pd.read_csv('data.csv'); #metodo para leer el csv y ahoora el algoritmo del mod read
  df= df[ df['Continent']== 'Europe' ] #filtro por continente
  
  countries = df['Country'].values #para obtener los valores de la columna
  percentages= df['World Population Percentage'].values #obtiene los valores
  
  charts.generate_pie_chart(countries, percentages)
  
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)
  
  
  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
    
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  #charts.generate_pie_chart(countries, percentages)



if __name__ == '__main__':
  run()