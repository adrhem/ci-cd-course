# Pasos para Generar el CI / CD
1. Crear repositorio en Github.
2. Subir cambios de tu aplicación. 
3. Posterior ir al ficha de Actions y crear Workflow.
4. Seleccionar Python Application.
5. Modificar el archivo para que haga las pruebas tal cual como se vio en el curso. En nuestro caso fue:
```
- name: Test with unittest
  run: |
    python tests.py
```
6. Crear Aplicación de Heroku.
7. Conectar repositorio creado en github en la ficha de Deploy.
8. Habilitar Deploys automáticos y revisar el checkbox de "Wait for CI to pass before deploy".  Esto permite revisar el flujo de las pruebas y que se publique automáticamente.
9. Hacer algún cambio y subir a producción. Si pasa la prueba se subirá automáticamente. En caso contrario no se hará la publicación.