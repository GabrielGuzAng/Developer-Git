A partir de un set de fondos y un set de fuentes de caracteres de keras se crea un dataset de caracteres sobre imágenes. Donde las mismas serán las x, y las y serán el caracter en sí
como sus coordenadas.
El modelo propuesto toma como modelo base el modelo ganador de Imagenet VGG16, el cuál es un modelo de redes profundas entrenado con 1000 clases.
El objetivo es aplicar una técnica de transfer learning el modelo para ajustarlo a nuestro fín, el cuál es que identifique al caracter de la imágen junto las coordenadas de sus aristas. Esto
se logra congelando los pesos de las capas mas profundas, borrando la última capa y suplantandola con una acorde a nuestras salidas. Subdividimos la rama principal de la reducción dimensional, hacia una dedicada al clasificador, con igual cantidad de salidas que nuestros caracteres, y otra rama con 8 salidas (4 pares de coordenadas).
Se entrena cada rama por separado. Se descongelan los pesos, y se realiza el ajuste fino.
